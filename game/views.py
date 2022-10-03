from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Game
from .serializers import GameSerializer, PostedGameSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def games(request, game_id=0):
    if request.method == 'GET':
        if game_id:
            game = get_object_or_404(Game, pk=game_id)
            serializer = GameSerializer(game)

            return Response(
                {
                    'status': 200,
                    'game': serializer.data
                },
                status=200
            )

        else:
            serializer = GameSerializer(Game.objects.all(), many=True)

            return Response(
                {
                    'status': 200,
                    'games': serializer.data,
                },
                status=200
            )

    elif request.method == 'POST':
        data = request.data
        data['author'] = request.user.id

        serializer = GameSerializer(data=data)

        try:
            serializer.is_valid(True)

        except ValidationError:
            return Response(
                {
                    'status': 400,
                    'description': 'data are invalid'
                },
                status=400
            )

        serializer.save()
        return Response(
            {
                'status': 201,
                'description': 'new game is successfully created.',
                'game': serializer.data,
            },
            status=201
        )

    elif request.method == "PUT":
        if game_id:
            data = request.data
            game = get_object_or_404(Game, pk=game_id)

            serializer = GameSerializer(game, data=data)

            try:
                serializer.is_valid(True)

            except ValidationError:
                return Response(
                    {'status': '400', 'description': 'data is invalid'},
                    status=400
                )

            serializer.save()

            return Response(
                {
                    'status': 200,
                    'description': 'game is updated',
                    'game': serializer.data,
                },
                status=200
            )

        else:
            return Response(
                {
                    'status': 400,
                    'description': "couldn't received game id"
                },
                status=400
            )

    elif request.method == "DELETE":
        if game_id:
            game = get_object_or_404(Game, pk=game_id)
            delete_id = game.id
            delete_title = game.title

            game.delete()

            return Response({
                'status': 200,
                'deleted_game_id': delete_id,
                'deleted_game_title': delete_title,
                'description': 'game is successfully deleted'
            },
                status=200
            )

        else:
            return Response({
                'status': 400,
                'description': "couldn't received game id"
            },
                status=400
            )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request, game_id):
    if request.method == 'POST':
        data = request.data

        if data['method'] == 'vote':

            game = get_object_or_404(Game, pk=game_id)
            serializer = GameSerializer(game)
            user = request.user
            votes = game.votes.all()

            left = votes.filter(side=False)[0]
            right = votes.filter(side=True)[0]

            # user is already voted
            if game.voted_users.filter(id=user.id).exists():
                if data['vote'] and left.users.filter(id=user.id).exists():
                    left.users.remove(user)
                    right.users.add(user)

                elif not data['vote'] and right.users.filter(id=user.id).exists():
                    right.users.remove(user)
                    left.users.add(user)

                right.save()
                left.save()

            else:
                v = votes.filter(side=data['vote'])[0]
                v.users.add(user)

                game.voted_users.add(user)

                v.save()
                game.save()

            return Response({
                'game': serializer.data
            },
                status=200
            )

        elif data['method'] == 'cancel':
            game = get_object_or_404(Game, pk=game_id)
            user = request.user

            if game.voted_users.filter(id=user.id).exists():
                v = game.votes.filter(side=data['vote'])[0]

                v.users.remove(user)
                game.voted_users.remove(user)

                v.save()
                game.save()

                return Response({
                    "status": 200,
                    "Description": "vote canceled"
                },
                    status=200
                )

            else:
                return Response({
                    "status": 406,
                    "Description": "user doesn't voted"
                },
                    status=406
                )


@api_view(['GET'])
def posted_games(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        serializer = PostedGameSerializer(user.games.all(), many=True)

        return Response({
            'status': 200,
            'user': user.username,
            'games': serializer.data
        },
            status=200
        )
