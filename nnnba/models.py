from django.db import models

class PlayerStats(models.Model):
    gp = models.FloatField(null=True)
    w = models.FloatField(null=True)
    w_pct = models.FloatField(null=True)
    min = models.FloatField(null=True)
    fgm = models.FloatField(null=True)
    fg_pct = models.FloatField(null=True)
    fg3m = models.FloatField(null=True)
    fg3a = models.FloatField(null=True)
    fg3_pct = models.FloatField(null=True)
    ftm = models.FloatField(null=True)
    fta = models.FloatField(null=True)
    ft_pct = models.FloatField(null=True)
    oreb = models.FloatField(null=True)
    dreb = models.FloatField(null=True)
    reb = models.FloatField(null=True)
    ast = models.FloatField(null=True)
    tov = models.FloatField(null=True)
    stl = models.FloatField(null=True)
    blk = models.FloatField(null=True)
    pf = models.FloatField(null=True)
    pfd = models.FloatField(null=True)
    pts = models.FloatField(null=True)
    plus_minus = models.FloatField(null=True)
    dd2 = models.FloatField(null=True)
    td3 = models.FloatField(null=True)
    off_rating = models.FloatField(null=True)
    def_rating = models.FloatField(null=True)
    net_rating = models.FloatField(null=True)
    ast_to = models.FloatField(null=True)
    efg_pct = models.FloatField(null=True)
    ts_pct = models.FloatField(null=True)
    usg_pct = models.FloatField(null=True)
    pie = models.FloatField(null=True)
    pts_2nd_chance = models.FloatField(null=True)
    point_guard = models.FloatField(null=True)
    shooting_guard = models.FloatField(null=True)
    small_forward = models.FloatField(null=True)
    power_forward = models.FloatField(null=True)
    center = models.FloatField(null=True)



class MLModel(models.Model):
    name = models.CharField(max_length=256)
    coefs = models.ForeignKey(PlayerStats, null=True)


class Player(models.Model):
    name = models.CharField(max_length=256)
    stats = models.ForeignKey(PlayerStats, null=True)
    
    paid = models.FloatField(default=0)
    projected_salaries = models.FloatField(default=0)
    
    def __str__(self):
        return self.name

class PlayerValue(models.Model):
    player = models.ForeignKey(Player)
    ml_model = models.ForeignKey(MLModel)

    worth = models.FloatField()
    difference = models.FloatField(null=True)

    def __str__(self):
        return self.player.name + ": " + str(self.worth)

