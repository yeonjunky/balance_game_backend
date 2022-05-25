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

        json_serializer = serializers.serialize('json', Game.objects.all())
        return JsonResponse(
            {"data": json.loads(json_serializer)}
        )

    elif request.method == 'POST':
        print(request.POST)
        choices = request.POST.getlist('choices')

        game = Game(choice_1_text=choices[0], choice_2_text=choices[1])

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
                game.id: [game.choice_1_text, game.choice_2_text],
            },

            status=201
        )
