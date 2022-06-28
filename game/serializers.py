from rest_framework import serializers

from .models import Game, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text', 'votes')


class GameSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'title', 'choices', )

    def create(self, validated_data):
        print(validated_data)
        choices_data = validated_data.pop('choices')
        game = Game.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(game=game, **choice_data)

        return game
