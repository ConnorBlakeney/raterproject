"""GameReview database model module"""
from django.db import models

class GameReview(models.Model):
    """GameReview database model"""
    rating = models.IntegerField() 
    content = models.CharField(max_length=1000)
    game = models.ForeignKey('raterprojectapi.Game', on_delete=models.CASCADE)
    player = models.ForeignKey('raterprojectapi.Player', on_delete=models.CASCADE)