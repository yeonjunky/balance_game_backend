from django.test import TestCase
from django.contrib.auth.models import User

from .models import Game, Choice
from .serializers import GameSerializer


# Create your tests here.
class GameSerializerTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='1234'
        )

    def test_create_question(self):
        title = "test"
        choice1 = "left"
        choice2 = 'right'

        serializer = GameSerializer(data={
            'title': title,
            'choices': [
                {
                    'text': choice1
                },
                {
                    'text': choice2
                }
            ],
            'author': self.user.id
        })

        serializer.is_valid(True)
        created_game = serializer.save()
        choices = created_game.choices.all()

        game = Game.objects.get(pk=created_game.id)

        self.assertEqual(title, game.title)
        self.assertEqual(choice1, game.choices.get(pk=choices[0].id).text)
        self.assertEqual(choice2, game.choices.get(pk=choices[1].id).text)

    def test_get_question(self):
        title = 'test'
        choice1 = 'left'
        choice2 = 'right'

        game = Game.objects.create(title=title, author=self.user)

        c1 = Choice.objects.create(text=choice1, game_id=game.id)
        c2 = Choice.objects.create(text=choice2, game_id=game.id)

        game.choices.add(c1)
        game.choices.add(c2)

        serializer = GameSerializer(game)

        data = serializer.data
        self.assertEqual(title, data.get('title'))
        self.assertEqual(data.get('choices')[0]['text'], choice1)
        self.assertEqual(data.get('choices')[1]['text'], choice2)
