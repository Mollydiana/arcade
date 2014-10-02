from django.contrib.auth.models import User
from django.db import models



class Game(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, related_name="games")

    def __unicode__(self):
        return u"{}".format(self.name)


class Score(models.Model):
    points = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, related_name="scores")

    def __unicode__(self):
        return u"{}".format(self.user)
