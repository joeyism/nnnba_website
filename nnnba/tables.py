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
    gp = tables.Column(orderable=False)
    w = tables.Column(orderable=False)
    w_pct = tables.Column(orderable=False)
    min = tables.Column(orderable=False)
    fgm = tables.Column(orderable=False)
    fg_pct = tables.Column(orderable=False)
    fg3m = tables.Column(orderable=False)
    fg3a = tables.Column(orderable=False)
    fg3_pct = tables.Column(orderable=False)
    ftm = tables.Column(orderable=False)
    fta = tables.Column(orderable=False)
    ft_pct = tables.Column(orderable=False)
    oreb = tables.Column(orderable=False)
    dreb = tables.Column(orderable=False)
    reb = tables.Column(orderable=False)
    ast = tables.Column(orderable=False)
    tov = tables.Column(orderable=False)
    stl = tables.Column(orderable=False)
    blk = tables.Column(orderable=False)
    pf = tables.Column(orderable=False)
    pfd = tables.Column(orderable=False)
    pts = tables.Column(orderable=False)

    class Meta: 
        attrs = {'class': 'paleblue', "width": "100%"}


class PlayerAdditionalStatsTable(tables.Table):
    plus_minus = tables.Column(orderable=False)
    dd2 = tables.Column(orderable=False)
    td3 = tables.Column(orderable=False)
    off_rating = tables.Column(orderable=False)
    def_rating = tables.Column(orderable=False)
    net_rating = tables.Column(orderable=False)
    ast_to = tables.Column(orderable=False)
    efg_pct = tables.Column(orderable=False)
    ts_pct = tables.Column(orderable=False)
    usg_pct = tables.Column(orderable=False)
    pie = tables.Column(orderable=False)
    pts_2nd_chance = tables.Column(orderable=False)

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


