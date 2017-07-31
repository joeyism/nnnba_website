from nnnba.models import Player
from nnnba_model import nnnba

def load_data():
    model = nnnba.NNNBA()

    stats_col = [ "gp", "w", "w_pct", "min", "fgm", "fg_pct", "fg3m", "fg3a", "fg3_pct", "ftm", "fta", "ft_pct", "oreb", "dreb", "reb", "ast", "tov", "stl", "blk", "pf", "pfd", "pts", "plus_minus", "dd2", "td3", "off_rating", "def_rating", "net_rating", "ast_to", "efg_pct", "ts_pct", "usg_pct", "pie", "pts_2nd_chance", "Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]

    for player_name in model.all_player_names:
        player_stats = model.getPlayerStats(player_name)
        kwargs_list = [("name", player_name)]

        for col in stats_col:
            if col in ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]:
                kwargs_list.append((col.lower().replace(" ", "_"), float(player_stats[col].values[0])))
            else:
                kwargs_list.append((col, float(player_stats[col.upper()].values[0])))

        value = model.getPlayerValue(player_name)
        kwargs_list.append(("paid", value["paid"]))
        kwargs_list.append(("projected_salaries", value["projected_salaries"]))

        kwargs = dict(kwargs_list)
        player = Player(**kwargs)
        player.id = int(player_stats.index[0])
        player.save()


if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    load_data()
