import django_tables2 as tables
from .models import Player, PlayerStats, PlayerValue
from django_tables2.utils import A 

class CurrencyColumn(tables.Column):
    def render(self,value):
        return '${:,.2f}'.format(value)

class MainPlayersTable(tables.Table):
    name = tables.LinkColumn('nnnba:player_stats', text=lambda record: record.name, args=[A('pk')], orderable=True)
    paid = CurrencyColumn()
    projected_salaries = CurrencyColumn()
    class Meta: 
        model = Player
        attrs = {'class': 'paleblue', 'width':'100%'}
        fields = ("name", "paid", "projected_salaries")
        empty_text = "There are no players with that name"

class PlayerStatsTable(tables.Table):
    PTS_PER_G = tables.Column(orderable=False, verbose_name="PTS")
    FG2_PCT = tables.Column(orderable=False, verbose_name="FG2%")
    FG3_PCT = tables.Column(orderable=False, verbose_name="FG3%")
    FG_PCT = tables.Column(orderable=False, verbose_name="FG%")
    AST_PER_G = tables.Column(orderable=False, verbose_name="AST")
    TRB_PER_G = tables.Column(orderable=False, verbose_name="TRB")
    FG2_PER_G = tables.Column(orderable=False, verbose_name="FG2")
    FG3_PER_G = tables.Column(orderable=False, verbose_name="FG3")
    TOV_PER_G = tables.Column(orderable=False, verbose_name="TOV")
    ORB_PER_G = tables.Column(orderable=False, verbose_name="ORB")
    PF_PER_G = tables.Column(orderable=False, verbose_name="PF")
    STL_PER_G = tables.Column(orderable=False, verbose_name="STL")
    FT_PER_G = tables.Column(orderable=False, verbose_name="FT")
    FTA_PER_G = tables.Column(orderable=False, verbose_name="FTA")
    FT_PCT = tables.Column(orderable=False, verbose_name="FT%")
    BLK_PER_G = tables.Column(orderable=False, verbose_name="BLK")

    class Meta: 
        attrs = {'class': 'paleblue', "width": "100%"}


class PlayerAdditionalStatsTable(tables.Table):
    AST_PCT = tables.Column(orderable=False, verbose_name="AST%")
    ORB_PCT = tables.Column(orderable=False, verbose_name="ORB%")
    DRB_PCT = tables.Column(orderable=False, verbose_name="DRB%")
    TRB_PCT = tables.Column(orderable=False, verbose_name="TRB%")
    TOV_PCT = tables.Column(orderable=False, verbose_name="TOV%")
    TS_PCT = tables.Column(orderable=False, verbose_name="TS%")
    FTA_PER_FGA_PCT = tables.Column(orderable=False, verbose_name="FTA_PER_FGA%")
    BLK_PCT = tables.Column(orderable=False, verbose_name="BLK%")
    STL_PCT = tables.Column(orderable=False, verbose_name="STL%")
    FG3A_PER_FGA_PCT = tables.Column(orderable=False, verbose_name="FG3A_PER_FGA%")
    OWS = tables.Column(orderable=False)
    DWS = tables.Column(orderable=False)
    WS = tables.Column(orderable=False)
    WS_PER_48 = tables.Column(orderable=False)
    OBPM = tables.Column(orderable=False)
    DBPM = tables.Column(orderable=False)
    BPM = tables.Column(orderable=False)
    PER = tables.Column(orderable=False)
    MIN_X_NET_RATING = tables.Column(orderable=False)
    EFG_PCT = tables.Column(orderable=False, verbose_name="EFG")
    USG_PCT = tables.Column(orderable=False, verbose_name="USG")
    VORP = tables.Column(orderable=False)

    class Meta: 
        attrs = {'class': 'paleblue', "width": "100%"}

class PlayerSalaryTable(tables.Table):
    paid = CurrencyColumn(orderable=False)
    projected_salaries = CurrencyColumn(orderable=False)

    class Meta: 
        attrs = {'class': 'paleblue', "width": "100%"}

class PlayerValueTable(PlayerSalaryTable):
    worth = CurrencyColumn(orderable=False)

    class Meta: 
        attrs = {'class': 'paleblue', "width": "100%"}

class PlayersValueByModel(tables.Table):
    worth = CurrencyColumn(orderable=True)
    name = tables.LinkColumn('nnnba:player_worth', text=lambda record: record.player.name, args=[A('player.id'), A('ml_model.name')], orderable=True, accessor='player.name')
    paid = CurrencyColumn(accessor="player.paid")
    difference = CurrencyColumn(verbose_name="Value Difference", accessor="difference")
    projected_salaries = CurrencyColumn(accessor="player.projected_salaries")

    class Meta: 
        model = PlayerValue
        attrs = {'class': 'paleblue', 'width':'100%'}
        fields = ("name", "paid", "projected_salaries", "difference", "worth")


