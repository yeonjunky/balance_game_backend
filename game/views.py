from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Game


# Create your views here.
@csrf_exempt
def games(request, game_id=0):
    if request.method == 'GET':
        if game_id:
            game = get_object_or_404(Game, pk=game_id)

            return JsonResponse(
                {"data": {
                    "id": game.id,
                    "first_choice": game.choice_1_text,
                    "second_choice": game.choice_2_text
                }})

        else:
            games_list = list(Game.objects.values())

            return JsonResponse(
                {"data": games_list}
            )

    elif request.method == 'POST':
        choices = json.loads(request.body)["choices"]

        game = Game(choice_1_text=choices['first_choice'], choice_2_text=choices['second_choice'])

        try:
            game.clean_fields()

        except ValidationError as e:
            return JsonResponse(
                {'status': '400', 'description': 'invalid choices text'},
                status=400
            )

        game.save()
        return JsonResponse(
            {
                'status': 201,
                'description': 'new game is successfully created.',
                f'id {game.id}': [game.choice_1_text, game.choice_2_text],
            },

            status=201
        )

    elif request.method == "PUT":
        if game_id:
            choices = json.loads(request.body)['choices']
            game = get_object_or_404(Game, pk=game_id)

            game.choice_1_text = choices['first_choice']
            game.choice_2_text = choices['second_choice']

            game.save()

            return JsonResponse({
                'status': '200',
                'description': 'game is updated',
                f'id {game.id}': [game.choice_1_text, game.choice_2_text],
            },

                status=200
            )

        else:
            JsonResponse({
                'status': '400',
                'description': "couldn't received game id"
            },

                status=400
            )

    elif request.method == "DELETE":
        pass
