from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Cinema(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=300)
    picture = models.ImageField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Sans(models.Model):
    movie = models.ForeignKey(to='Movie', on_delete=models.CASCADE)
    cinema = models.ForeignKey(to='Cinema', on_delete=models.CASCADE)
    play_at = models.DateTimeField()

    def __str__(self):
        return f'{self.movie.name} play at {self.cinema.name} on {self.play_at}'


class Ticket(models.Model):
    sans = models.ForeignKey(to='Sans', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | {self.sans.play_at}'


class Actor(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True , blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
    movie = models.ForeignKey(to='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | movie : {self.movie.name} | comment : {self.text} | time : {self.date}'
    

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Criticism(models.Model):
    description = models.TextField()
    read_time = models.IntegerField()
    movie = models.ForeignKey(to='Movie', on_delete=models.CASCADE)


    def __str__(self):
        return f' movie : {self.movie.name} | description : {self.description} | readtime: {self.read_time}'