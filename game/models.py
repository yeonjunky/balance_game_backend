from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=256)
    choice_1_text = models.CharField(max_length=256)
    choice_2_text = models.CharField(max_length=256)
    vote_1 = models.PositiveIntegerField(default=0)
    vote_2 = models.PositiveIntegerField(default=0)

    def clean(self):
        if not self.title:
            raise ValidationError("Title is empty")

        if self.choice_1_text is None or self.choice_2_text is None:
            raise ValidationError("At least one choice is blank")

        elif self.choice_1_text == self.choice_2_text:
            raise ValidationError("The choices' text is the same")

    def __str__(self):
        return self.title


class Choice(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    voted_num = models.PositiveIntegerField(default=0)

    def vote(self):
        self.voted_num += 1
        self.save()

    def __str__(self):
        return self.text
