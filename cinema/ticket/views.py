from django.shortcuts import render
from ticket.serializer import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from ticket.models import Cinema, Movie, Ticket, Actor, Comment, Genre,  Criticism
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class CinemaListCreate(ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['capacity']


class CinemaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['genres']
    ordering_fields = ['price', 'score', 'votes']


class MovieRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['genres']
    ordering_fields = ['price', 'score', 'votes']


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class ActorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveUpdateDestroySerializer


class GenreListCreate(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class GenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class CriticismListCreate(ListCreateAPIView):
    queryset = Criticism.objects.all()
    serializer_class = CriticismSerializer


class CriticismRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Criticism.objects.all()
    serializer_class = CriticismRetrieveUpdateDestroySerializer