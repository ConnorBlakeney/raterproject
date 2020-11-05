from django.db import models
from django.conf import settings

class Category(models.Model):
    """Category model class"""
    type = models.CharField(max_length=20)
