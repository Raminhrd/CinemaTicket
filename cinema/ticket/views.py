from django.shortcuts import render
from ticket.serializer import *
from ticket.models import Cinema, Movie, Ticket, Actor, Comment, Genre,  Criticism
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class CinemaListCreate(ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaRetrieveUpdateDestroySerializer


class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieRetrieveUpdateDestroySerializer


class SansListCreate(ListCreateAPIView):
    queryset = Sans.objects.all()
    serializer_class = SansSerializer


class SansRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sans.objects.all()
    serializer_class = SansRetrieveUpdateDestroySerializer


class TicketListCreate(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketRetrieveUpdateDestroySerializer


class ActorListCreate(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorRetrieveUpdateDestroySerializer


class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveUpdateDestroySerializer


class GenreListCreate(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveUpdateDestroySerializer


class CriticismListCreate(ListCreateAPIView):
    queryset = Criticism.objects.all()
    serializer_class = CriticismSerializer


class CriticismRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Criticism.objects.all()
    serializer_class = CriticismRetrieveUpdateDestroySerializer