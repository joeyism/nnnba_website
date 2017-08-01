from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Player
from .tables import MainPlayersTable
from django_tables2 import RequestConfig


def main(request):
    players = MainPlayersTable(Player.objects.all())
    RequestConfig(request).configure(players)
    return render(request, 'nnnba/main.html', { "players": players })


def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    stats = player.stats.__dict__.copy()
    del stats["id"]
    del stats["_state"]
    return render(request, 'nnnba/player.html', { "stats": stats.items(), "player": player.__dict__ })

