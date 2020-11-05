"""GameImage database model module"""
from raterprojectapi.models.player import Player
from django.db import models

class GameImage(models.Model):
    """GameImage database model"""
    image = models.ImageField(upload_to='game_images', height_field=None, width_field=None, max_length=None, null=True)
    game = models.ForeignKey('raterprojectapi.Game', on_delete=models.CASCADE)
    Player = models.ForeignKey('raterprojectapi.Player', on_delete=models.CASCADE)