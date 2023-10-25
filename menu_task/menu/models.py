from django.db import models


# Create your models here.
class ListItems(models.Model):
    menu = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
