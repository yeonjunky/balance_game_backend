from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

from .models import Game
from .serializers import GameSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def games(request, game_id=0):
    if request.method == 'GET':
        if game_id:
            game = get_object_or_404(Game, pk=game_id)

            serializer = GameSerializer(game)

            return Response(serializer.data)

        else:
            serializer = GameSerializer(Game.objects.all(), many=True)

            return Response(serializer.data)

    elif request.method == 'POST':
        body = json.loads(request.body)

        title = body["title"]
        choices = body["choices"]

        game = Game(title=title, choice_1_text=choices['first_choice'], choice_2_text=choices['second_choice'])

        try:
            game.clean_fields()

        except ValidationError as e:
            return Response(
                {'status': '400', 'description': 'data are invalid'},
                status=400
            )

        game.save()
        return Response(
            {
                'status': 201,
                'description': 'new game is successfully created.',
                f'id {game.id}': [game.title, game.choice_1_text, game.choice_2_text],
            },

            status=201
        )

    elif request.method == "PUT":
        if game_id:
            body = json.loads(request.body)
            title = body['title']
            choices = body['choices']
            game = get_object_or_404(Game, pk=game_id)

            game.title = title

            game.choice_1_text = choices['first_choice']
            game.choice_2_text = choices['second_choice']

            game.save()

            return Response({
                'status': '200',
                'description': 'game is updated',
                f'id {game.id}': [game.title, game.choice_1_text, game.choice_2_text],
            },

                status=200
            )

        else:
            return Response({
                'status': '400',
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
                "deleted_id": delete_id,
                "deleted_title": delete_title,
            },
                status=200
            )

        else:
            return Response({
                'status': '400',
                'description': "couldn't received game id"
            },
                status=400
            )
