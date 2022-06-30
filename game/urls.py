from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.games),
    path('games/<int:game_id>', views.games),
    path('vote/<int:vote_id>', views.vote),
]
