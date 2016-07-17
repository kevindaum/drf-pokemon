from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    combat_power = models.PositiveSmallIntegerField()


class Trainer(models.Model):
    name = models.CharField(max_length=30)
    pokemon = models.ManyToManyField('Pokemon')
    team = models.ForeignKey('Team')
