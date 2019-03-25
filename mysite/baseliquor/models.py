from django.db import models

# Create your models here.
class BaseLiquor(models.Model):
    name = models.CharField(max_length=100)
    pic = models.URLField(blank=True)
    origin = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.TextField(blank=True)