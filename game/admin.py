from django.contrib import admin

from .models import Game, Choice, Vote


# Register your models here.
class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class GameAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [
        VoteInline,
    ]


admin.site.register(Game, GameAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote)
