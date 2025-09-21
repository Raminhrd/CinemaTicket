from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Cinema(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=300)
    picture = models.ImageField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    time =  models.TimeField()
    score = models.PositiveIntegerField(validators=[MinValueValidator(0,0), MaxValueValidator(5,0)])
    votes = models.IntegerField()
    trailer = models.FileField(null=True , blank=True)
    description = models.TextField()
    director = models.CharField(max_length=100)
    picture = models.ImageField(null=True , blank=True)
    actors = models.ManyToManyField("Actor")
    genres = models.ManyToManyField("Genre")


class Sans(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)
    play_at = models.DateTimeField()


class Ticket(models.Model):
    sans = models.ForeignKey(to='Sans', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True , blank=True)


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
    movie = models.ForeignKey(to='Movie', on_delete=models.CASCADE)
    

class Genre(models.Model):
    name = models.CharField(max_length=100)


class Criticism(models.Model):
    description = models.TextField()
    read_time = models.IntegerField()
    movie = models.ForeignKey(to='Movie', on_delete=models.CASCADE)