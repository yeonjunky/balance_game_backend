from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.games),
    path('games/<int:game_id>/', views.games),
    path('games/<int:game_id>/vote/', views.vote),
    path('games/user/<int:user_id>/', views.posted_games),
]
