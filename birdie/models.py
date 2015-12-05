from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=64)
    street_number = models.IntegerField()
    street = models.CharField(max_length=256)
    postcode = models.CharField(max_length=8)
    description = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Game(models.Model):
    organiser = models.ForeignKey(User, related_name='organised_games')
    players = models.ManyToManyField(User, related_name='games')
    name = models.CharField(max_length=64)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=1024)
    datetime = models.DateTimeField()
    duration = models.IntegerField()
    max_players = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['datetime']


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    timestamp = models.DateTimeField()
    author = models.ForeignKey(User, related_name='comments')
    game = models.ForeignKey(Game, related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['timestamp']