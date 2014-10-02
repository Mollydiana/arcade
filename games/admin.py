from django.contrib import admin
from games.models import Game, Score, Profile

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Score)