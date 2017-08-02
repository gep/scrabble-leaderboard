from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField('Created')

class Score(models.Model):
    score = models.IntegerField(default=0)
    Player = models.ForeignKey(Player, related_name='%(class)s_player')

class Game(models.Model):
    Score1 = models.ForeignKey(Score, related_name='%(class)s_score1')
    Score2 = models.ForeignKey(Score, related_name='%(class)s_Score2')
    created_at = models.DateTimeField('Created')
    Winner = models.ForeignKey(Player, related_name='%(class)s_winner')
