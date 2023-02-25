from django.db import models

# Create your models here.
class Suit(models.Model):

    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    