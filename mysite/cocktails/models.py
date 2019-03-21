from django.db import models

# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    pic = models.URLField(blank=True)
    link = models.URLField(blank=True)
