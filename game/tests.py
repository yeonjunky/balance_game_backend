from django.test import TestCase
from django.contrib.auth.models import User

from .models import Game
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





