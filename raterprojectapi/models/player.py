from django.db import models
from django.conf import settings

class Player(models.Model):
    """Player model class"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"