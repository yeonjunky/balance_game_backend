from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Game(models.Model):
    choice_1_text = models.CharField(max_length=256)
    choice_2_text = models.CharField(max_length=256)

    def clean(self):
        if self.choice_1_text is None or self.choice_2_text is None:
            raise ValidationError("At least one choice is blank")

        elif self.choice_1_text == self.choice_2_text:
            raise ValidationError("The choices' text is the same")
