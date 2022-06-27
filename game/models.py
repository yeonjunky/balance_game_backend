from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=256)

    def clean(self):
        if not self.title:
            raise ValidationError("Title is empty")

    def __str__(self):
        return self.title


class Choice(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    votes = models.PositiveIntegerField(default=0)

    def vote(self):
        self.votes += 1
        self.save()

    def clean(self):
        if not self.text:
            raise ValidationError("text is empty")

    def __str__(self):
        return self.text
