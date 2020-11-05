"""GameCategory database model module"""
from django.db import models

class GameCategory(models.Model):
    """GameCategory database model"""
    game = models.ForeignKey('raterprojectapi.Game', on_delete=models.CASCADE, related_name="game_category")
    category = models.ForeignKey('raterprojectapi.Category', on_delete=models.CASCADE, related_name="game_category")