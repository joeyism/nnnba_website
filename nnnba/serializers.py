from rest_framework import serializers
from .models import PlayerStats

class PlayerStatsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlayerStats
        fields = ( "gp", "w", "w_pct", "min", "fgm", "fg_pct", "fg3m", "fg3a", "fg3_pct", "ftm", "fta", "ft_pct", "oreb", "dreb", "reb", "ast", "tov", "stl", "blk", "pf", "pfd", "pts", "plus_minus", "dd2", "td3", "off_rating", "def_rating", "net_rating", "ast_to", "efg_pct", "ts_pct", "usg_pct", "pie", "pts_2nd_chance")

