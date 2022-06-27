from rest_framework import serializers

from .models import Game, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True)

    class Meta:
        model = Game
        fields = '__all__'
