from django.db import models
from django.db.models.base import Model

from django.db import models
from django.conf import settings

class Game(models.Model):
    """Game model class"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    designer = models.CharField(max_length=30)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    play_time = models.IntegerField()
    player_age = models.IntegerField()
    