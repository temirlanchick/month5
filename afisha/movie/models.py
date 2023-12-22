from django.db import models


class Director(models.Model):
    name = models.CharField


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    duration = models.IntegerField
    director = models.ForeignKey


class Review(models.Model):
    text = models.TextField
    movie = models.ForeignKey






