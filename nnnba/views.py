from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from rest_framework import viewsets
from chartit import DataPool, Chart
from rest_framework.response import Response

from .models import Player, MLModel, PlayerValue
from .tables import MainPlayersTable, PlayerStatsTable, PlayerAdditionalStatsTable, PlayerSalaryTable, PlayerValueTable, PlayersValueByModel
from .filters import MainPlayersFilter
from .serializers import PlayerStatsSerializer




def main(request):
    filter_name = request.GET.get('name', '')
    if filter_name == '':
        players = MainPlayersTable(Player.objects.all())
    else:
        players = MainPlayersTable(Player.objects.filter(name__icontains=filter_name))

    RequestConfig(request).configure(players)
    f = MainPlayersFilter(request.GET, queryset=Player.objects.all())

    return render(request, 'nnnba/main.html', { "players": players , "filter": f})


def player_stats(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    stats = PlayerStatsTable([Player.objects.get(pk=player_id).stats.__dict__])
    additional_stats = PlayerAdditionalStatsTable([Player.objects.get(pk=player_id).stats.__dict__])
    salary = PlayerSalaryTable([player])

    return render(request, 'nnnba/player.html', { "stats": stats, "additional_stats": additional_stats, "player": player.__dict__, "salary": salary, "model_name": ""})


def player_worth(request, player_id, model_name):
    player = get_object_or_404(Player, pk=player_id)
    ml_model = get_object_or_404(MLModel, name=model_name)

    player_value = get_object_or_404(PlayerValue, player=player, ml_model=ml_model)

    stats = PlayerStatsTable([Player.objects.get(pk=player_id).stats.__dict__])
    additional_stats = PlayerAdditionalStatsTable([Player.objects.get(pk=player_id).stats.__dict__])

    value_dict = {**player_value.__dict__ , **player.__dict__ }
    value = PlayerValueTable([value_dict])

    return render(request, 'nnnba/player_value.html', { "stats": stats, "additional_stats": additional_stats, "player": player.__dict__, "value": value, "model_name": model_name})

def model_details(request, model_name):
    if model_name == "models":
        model_name = "avg"
    ml_model = get_object_or_404(MLModel, name=model_name)
    filter_name = request.GET.get('name', '')

    if filter_name == '':
        player_value_set = ml_model.playervalue_set.order_by("-worth")
        player_value_table = PlayersValueByModel(player_value_set)
    else:
        player_value_set = ml_model.playervalue_set.filter(player__name__icontains=filter_name).order_by("-worth")
        player_value_table = PlayersValueByModel(player_value_set)


    RequestConfig(request).configure(player_value_table)
    f = MainPlayersFilter(request.GET, queryset=Player.objects.all())

    return render(request, 'nnnba/model_details.html', {"player_value_table": player_value_table, "model_name": model_name, "models_with_coefs": ["ridge", "lasso", "linear regression", "bayes ridge", "elasticnet"], "filter": f})

class CoefViewSet(viewsets.ViewSet):
    lookup_field = 'model_name'

    def retrieve(self, request, model_name=None):
        ml_model = get_object_or_404(MLModel, name=model_name)
        queryset = ml_model.coefs
        serializer = PlayerStatsSerializer(queryset)
        return Response(serializer.data)


