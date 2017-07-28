from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def main(request):
    return render(request, 'nnnba/main.html', {})

def player(request, player_id):
    return render(request, 'nnnba/player.html', {})

