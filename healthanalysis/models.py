from django.db import models
from account.models import User


# Create your models here.


class HealthAnalysis(models.Model):
    """
    HealthAnalysis model
    """
    name: str = models.CharField(max_length=100)
    bbox = models.JSONField()
    coordinates = models.JSONField()
    path = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
