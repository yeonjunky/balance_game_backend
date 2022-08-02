from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=256)
    voted_users = models.ManyToManyField(User, related_name='voted_users', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def clean(self):
        if not self.title:
            raise ValidationError("Title is empty")

    def __str__(self):
        return self.title


class Choice(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=256)

    def vote(self):
        self.votes += 1
        self.save()

    def clean(self):
        if not self.text:
            raise ValidationError("text is empty")

    def __str__(self):
        return self.text


class Vote(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None, related_name='votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default=None, related_name='votes')
    users = models.ManyToManyField(User, related_name='users')
    side = models.BooleanField(default=None)  # left side choice : False, right side choice : True
