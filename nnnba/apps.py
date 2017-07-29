from django.apps import AppConfig
from ..nnnba_model import nnnba
from .models import Player


class NNNbaConfig(AppConfig):
    name = 'nnnba'

    def ready(self):
        nnnba_model = nnnba.NNNBA()

        for player_name in nnnba_model.all_player_names:
            stats = nnnba.getPlayerStats(player_name)

