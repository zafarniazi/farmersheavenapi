from django.db import models
from account.models import User


class blog(models.Model):
    """
    blog model
    """
    title: str = models.CharField(max_length=100)
    content: str = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
