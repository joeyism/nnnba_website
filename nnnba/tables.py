import django_tables2 as tables
from .models import Player
from django_tables2.utils import A 

class MainPlayersTable(tables.Table):
    name = tables.LinkColumn('nnnba:main_player', text=lambda record: record.name, args=[A('pk')], orderable=True)
    class Meta:
        model = Player
        attrs = {'class': 'paleblue'}
        fields = ("name", "paid", "projected_salaries")
