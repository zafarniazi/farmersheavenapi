from django.db import models
# Create your models here.


class Contactus(models.Model):
    """
  contactus model 
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Messages"
        verbose_name_plural = "Message"
