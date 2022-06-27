from django.contrib import admin

from .models import Game, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class GameAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Game, GameAdmin)
admin.site.register(Choice)
