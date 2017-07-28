from django.db import models


class PlayerStats(models.Model):
    gp = models.FloatField()
    w = models.FloatField()
    w_pct = models.FloatField()
    min = models.FloatField()
    fgm = models.FloatField()
    fg_pct = models.FloatField()
    fg3m = models.FloatField()
    fg3a = models.FloatField()
    fg3_pct = models.FloatField()
    ftm = models.FloatField()
    fta = models.FloatField()
    ft_pct = models.FloatField()
    oreb = models.FloatField()
    dreb = models.FloatField()
    reb = models.FloatField()
    ast = models.FloatField()
    tov = models.FloatField()
    stl = models.FloatField()
    blk = models.FloatField()
    pf = models.FloatField()
    pfd = models.FloatField()
    pts = models.FloatField()
    plus_minus = models.FloatField()
    dd2 = models.FloatField()
    td3 = models.FloatField()
    off_rating = models.FloatField()
    def_rating = models.FloatField()
    net_rating = models.FloatField()
    ast_to = models.FloatField()
    efg_pct = models.FloatField()
    ts_pct = models.FloatField()
    usg_pct = models.FloatField()
    pie = models.FloatField()
    pts_2nd_chanCE = models.FloatField()
    point_guard = models.FloatField()
    shooting_guard = models.FloatField()
    small_forward = models.FloatField()
    power_forward = models.FloatField()
    center = models.FloatField()

    class Meta:
        abstract = True


class MLModel(models.Model):
    name = models.CharField(max_length=256)


class Player(PlayerStats):
    name = models.CharField(max_length=256)
    
    paid = models.FloatField(default=0)
    future_salary = models.FloatField(default=0)

class PlayerValue(models.Model):
    player = models.ForeignKey(Player)
    model_name = models.ForeignKey(MLModel)

    worth = models.FloatField()


class Coefficients(PlayerStats):
    model_name = models.ForeignKey(MLModel)


