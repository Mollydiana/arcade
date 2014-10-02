from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):

    def __unicode__(self):
        return self.username

class Game(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(default=0, null=True, blank=True)
    profile = models.ForeignKey(Profile, related_name="games")

    def __unicode__(self):
        return u"{}".format(self.name)


class Score(models.Model):
    points = models.IntegerField(default=0, null=True, blank=True)
    profile = models.ForeignKey(Profile, related_name="scores")

    def __unicode__(self):
        return u"{}".format(self.user)
