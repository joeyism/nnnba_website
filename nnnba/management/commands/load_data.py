from nnnba.models import Player, MLModel, PlayerStats
from nnnba_model import nnnba
from django.core.management.base import BaseCommand, CommandError

stats_col = [ "gp", "w", "w_pct", "min", "fgm", "fg_pct", "fg3m", "fg3a", "fg3_pct", "ftm", "fta", "ft_pct", "oreb", "dreb", "reb", "ast", "tov", "stl", "blk", "pf", "pfd", "pts", "plus_minus", "dd2", "td3", "off_rating", "def_rating", "net_rating", "ast_to", "efg_pct", "ts_pct", "usg_pct", "pie", "pts_2nd_chance", "Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]

def add_players(model):

    for player_name in model.all_player_names:
        player_stats = model.getPlayerStats(player_name)

        value = model.getPlayerValue(player_name)

        player = Player(name=player_name, paid=value["paid"], projected_salaries=value["projected_salaries"])
        player.id = int(player_stats.index[0])
        player.save()
 

        kwargs_list = []

        for col in stats_col:
            if col in ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]:
                kwargs_list.append((col.lower().replace(" ", "_"), float(player_stats[col].values[0])))
            else:
                kwargs_list.append((col, float(player_stats[col.upper()].values[0])))

        kwargs = dict(kwargs_list)
        stats = PlayerStats(**kwargs)
        stats.save()
        player.stats = stats
        player.save()
        

def add_model_coef_player_values(model):

    for model_name in model.showAvailableModels():
        ml_model = MLModel(name=model_name)
        ml_model.save()

        if model_name in ["ridge", "linear regression", "lasso", "elasticnet", "bayes ridge"]:
            coef = model.getCoefFromModel(model_name)
            kwargs_list = []
            for col in stats_col:
                if col in ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]:
                    kwargs_list.append((col.lower().replace(" ", "_"), float(coef["coef"][col])))
                else:
                    kwargs_list.append((col, float(coef["coef"][col.upper()])))

            kwargs = dict(kwargs_list)
            stats = PlayerStats(**kwargs)
            stats.save()
            ml_model.coefs = stats
            ml_model.save()

        for player_name in model.all_player_names:
            player = Player.objects.get(name=player_name)
            value = model.getPlayerValue(player_name)
            player.playervalue_set.create(ml_model=ml_model, worth=float(value["worth"]))
            player.save()


def load_data():
    model = nnnba.NNNBA()
    add_players(model)
    add_model_coef_player_values(model)


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_data()



if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    load_data()

