from django.db import models

def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            _('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )

class PlayerStats(models.Model):
    TOV_PCT = models.FloatField(null = True, validators=[validate_decimals])
    TS_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FG2_PCT = models.FloatField(null = True, validators=[validate_decimals])
    TRB_PCT = models.FloatField(null = True, validators=[validate_decimals])
    PTS_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    FG2_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    TOV_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    ORB_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    BPM = models.FloatField(null = True, validators=[validate_decimals])
    PF_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    USG_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FG_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FG3_PCT = models.FloatField(null = True, validators=[validate_decimals])
    DRB_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FTA_PER_FGA_PCT = models.FloatField(null = True, validators=[validate_decimals])
    STL_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    BLK_PCT = models.FloatField(null = True, validators=[validate_decimals])
    OWS = models.FloatField(null = True, validators=[validate_decimals])
    WS = models.FloatField(null = True, validators=[validate_decimals])
    FG3A_PER_FGA_PCT = models.FloatField(null = True, validators=[validate_decimals])
    EFG_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FG3_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    AST_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    FT_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    FTA_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    BLK_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    ORB_PCT = models.FloatField(null = True, validators=[validate_decimals])
    STL_PCT = models.FloatField(null = True, validators=[validate_decimals])
    VORP = models.FloatField(null = True, validators=[validate_decimals])
    DBPM = models.FloatField(null = True, validators=[validate_decimals])
    WS_PER_48 = models.FloatField(null = True, validators=[validate_decimals])
    DWS = models.FloatField(null = True, validators=[validate_decimals])
    PER = models.FloatField(null = True, validators=[validate_decimals])
    OBPM = models.FloatField(null = True, validators=[validate_decimals])
    TRB_PER_G = models.FloatField(null = True, validators=[validate_decimals])
    AST_PCT = models.FloatField(null = True, validators=[validate_decimals])
    FT_PCT = models.FloatField(null = True, validators=[validate_decimals])
    MIN_X_NET_RATING = models.FloatField(null = True, validators=[validate_decimals])

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

