from rest_framework import serializers
from .models import PlayerStats

class PlayerStatsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlayerStats
        fields = ( 'TOV_PCT', 'TS_PCT', 'FG2_PCT', 'TRB_PCT', 'PTS_PER_G', 'FG2_PER_G', 'TOV_PER_G', 'ORB_PER_G', 'BPM', 'PF_PER_G', 'USG_PCT', 'FG_PCT', 'FG3_PCT', 'DRB_PCT', 'FTA_PER_FGA_PCT', 'STL_PER_G', 'BLK_PCT', 'OWS', 'WS', 'FG3A_PER_FGA_PCT', 'EFG_PCT', 'FG3_PER_G', 'AST_PER_G', 'FT_PER_G', 'FTA_PER_G', 'BLK_PER_G', 'ORB_PCT', 'STL_PCT', 'VORP', 'DBPM', 'WS_PER_48', 'DWS', 'PER', 'OBPM', 'TRB_PER_G', 'AST_PCT', 'FT_PCT', 'MIN_X_NET_RATING')

