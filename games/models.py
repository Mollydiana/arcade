from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.name)


class Game(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(default=0, null=True, blank=True)
    player = models.ForeignKey(Player, related_name="games")

    def __unicode__(self):
        return u"{}".format(self.name)
