from django.contrib import admin

# Register your models here.
from dashboard.models import Player, Score, Game

admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Game)

