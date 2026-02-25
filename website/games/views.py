from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import  Game

def game_list(request):
    """Отображает список всех игр/приложений."""
    games = Game.objects.all()
    context = {
        'games': games,
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'games/game_list.html', context)

def game_detail(request, pk):
    """Отображает детальную информацию об одной игре/приложении."""
    game = get_object_or_404(Game, pk=pk)
    context = {
        'game': game,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'games/game_detail.html', context)
