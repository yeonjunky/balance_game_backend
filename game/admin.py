from django.contrib import admin

from .models import Game, Choice


# Register your models here.
admin.site.register(Game)
admin.site.register(Choice)