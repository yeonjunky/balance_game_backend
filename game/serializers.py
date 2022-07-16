from rest_framework import serializers

from .models import Game, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'text', 'votes')

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class GameSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'title', 'choices', )

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        game = Game.objects.create(**validated_data)

        for i in range(2):
            c = Choice.objects.create(game=game, **choices_data[i])
            v = Vote.objects.create(game=game, choice=c, side=bool(i))

            c.save()
            v.save()

        return game

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choices')

        instance.title = validated_data.get('title', instance.title)
        choices = list(instance.choices.all())

        for choice_data in choices_data:
            c = choices.pop(0)
            c.text = choice_data.get('text', c.text)
            c.save()

        instance.save()

        return instance
