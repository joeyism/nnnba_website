from nnnba.models import Player, MLModel, PlayerStats
from nnnba_model import nnnba
from django.core.management.base import BaseCommand, CommandError

stats_col = [ 'tov_pct', 'ts_pct', 'fg2_pct', 'trb_pct', 'pts_per_g', 'fg2_per_g', 'tov_per_g', 'orb_per_g', 'bpm', 'pf_per_g', 'usg_pct', 'fg_pct', 'fg3_pct', 'drb_pct', 'fta_per_fga_pct', 'stl_per_g', 'blk_pct', 'ows', 'ws', 'fg3a_per_fga_pct', 'efg_pct', 'fg3_per_g', 'ast_per_g', 'ft_per_g', 'fta_per_g', 'blk_per_g', 'orb_pct', 'stl_pct', 'vorp', 'dbpm', 'ws_per_48', 'dws', 'per', 'obpm', 'trb_per_g', 'ast_pct', 'ft_pct', 'MIN_X_NET_RATING']

def add_players(model):

    for player_name in model.all_player_names:
        player_stats = model.getPlayerStats(player_name)

        value = model.getPlayerValue(player_name)

        player = Player(name=player_name, paid=value["paid"], projected_salaries=value["projected_salaries"])
        player.id = int(player_stats.index[0])
        player.save()
 

        kwargs_list = []

        for col in stats_col:
            if col in ["MIN_X_NET_RATING"]:
                kwargs_list.append((col, float(player_stats[col].values[0])))
            else:
                kwargs_list.append((col.upper(), float(player_stats[col].values[0])))

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
                if col in ["MIN_X_NET_RATING"]:
                    kwargs_list.append((col, float(coef["coef"][col])))
                else:
                    kwargs_list.append((col.upper(), float(coef["coef"][col])))

            kwargs = dict(kwargs_list)
            stats = PlayerStats(**kwargs)
            stats.save()
            ml_model.coefs = stats
            ml_model.save()

        for player_name in model.all_player_names:
            player = Player.objects.get(name=player_name)
            value = model.getPlayerValue(player_name, model_type=model_name)
            player.playervalue_set.create(ml_model=ml_model, worth=float(value["worth"]), difference=float(value["worth"] - value["projected_salaries"]))
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

