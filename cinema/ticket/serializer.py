from ticket.models import Cinema, Movie, Sans, Ticket, Actor, Comment, Genre, Criticism
from rest_framework.serializers import ModelSerializer


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name', 'adress', 'picture', 'capacity']


class CinemaRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name', 'adress', 'picture', 'capacity']


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','price','time', 'score','votes','trailer','description','director','picture','actors','genres' ]


class MovieRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','price','time', 'score','votes','trailer','description','director','picture','actors','genres' ]


class SansSerializer(ModelSerializer):
    class Meta:
        model = Sans
        fields = ['movie', 'cinema', 'play_at']


class SansRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Sans
        fields = ['movie', 'cinema', 'play_at']


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'sans']


class TicketRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'sans']


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'picture']


class ActorRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'picture']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'date','text', 'movie']


class CommentRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'date','text', 'movie']

    
class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class GenreRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class CriticismSerializer(ModelSerializer):
    class Meta:
        model = Criticism
        fields = ['description', 'read_time', 'movie']


class CriticismRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Criticism
        fields = ['description', 'read_time', 'movie']