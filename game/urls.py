from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.games),
    path('games/<int:game_id>/', views.games),
    path('games/<int:game_id>/vote/', views.vote),
    path('games/user/<str:username>/', views.posted_games),
]
