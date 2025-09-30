from django.shortcuts import render
from ticket.serializer import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from ticket.models import Cinema, Movie, Ticket, Actor, Comment, Genre,  Criticism
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions



class CinemaListCreate(ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['capacity']

    def get_permissions(self):
        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
        

class CinemaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['genres']
    ordering_fields = ['price', 'score', 'votes']

    def get_permissions(self):
        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class MovieRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['genres']
    ordering_fields = ['price', 'score', 'votes']

    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    

class SansListCreate(ListCreateAPIView):
    queryset = Sans.objects.all()
    serializer_class = SansSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    

class SansRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sans.objects.all()
    serializer_class = SansRetrieveUpdateDestroySerializer


    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    

class TicketListCreate(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    

class TicketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketRetrieveUpdateDestroySerializer

    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    

class ActorListCreate(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    

class ActorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Actor.objects.all()
        return Actor.objects.filter(user=user)   

class CommentListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveUpdateDestroySerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(user=user)

class GenreListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class GenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class CriticismListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Criticism.objects.all()
    serializer_class = CriticismSerializer


class CriticismRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Criticism.objects.all()
    serializer_class = CriticismRetrieveUpdateDestroySerializer

    def get_permissions(self):
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]