from django.db import models


class World(models.Model):
    name = models.CharField(max_length=70, blank=True, default='Unknown')
    species = models.CharField(max_length=200, blank=True, default='None')
    galaxy = models.CharField(max_length=200, blank=True, default='Unknown')
    gas = models.BooleanField(default=False)
    population = models.IntegerField()
    birth_date = models.DateTimeField(auto_now_add=True, blank=True)
