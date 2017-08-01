import django_filters
from .models import Player
from .tables import MainPlayersTable

class MainPlayersFilter(django_filters.FilterSet):

    class Meta:
        model = Player
        fields = ["name"]
        order_by = ["pk"]
