from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Game


# Create your views here.
@csrf_exempt
def games(request):
    if request.method == 'GET':

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
                'status': '201',
                'description': 'new game is successfully created.',
                f'id {game.id}': [game.choice_1_text, game.choice_2_text],
            },

            status=201
        )
