from ticket.models import Cinema, Movie, Sans, Ticket, Actor, Comment, Genre, Criticism
from rest_framework.serializers import ModelSerializer , StringRelatedField


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name', 'adress', 'picture', 'capacity']


class CinemaRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name', 'adress', 'picture', 'capacity']


class MovieSerializer(ModelSerializer):
    actors = StringRelatedField(many=True)
    genres = StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['name','price','time', 'score','votes','trailer','description','director','picture','actors','genres' ]


class MovieRetrieveUpdateDestroySerializer(ModelSerializer):
    actors = StringRelatedField(many=True)
    genres = StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['name','price','time', 'score','votes','trailer','description','director','picture','actors','genres' ]


class SansSerializer(ModelSerializer):
    movie = StringRelatedField()
    cinema = StringRelatedField()
    class Meta:
        model = Sans
        fields = ['movie', 'cinema', 'play_at']


class SansRetrieveUpdateDestroySerializer(ModelSerializer):
    movie = StringRelatedField()
    cinema = StringRelatedField()
    class Meta:
        model = Sans
        fields = ['movie', 'cinema', 'play_at']


class TicketSerializer(ModelSerializer):
    user = StringRelatedField()
    sans = StringRelatedField()
    class Meta:
        model = Ticket
        fields = ['user', 'sans']


class TicketRetrieveUpdateDestroySerializer(ModelSerializer):
    user = StringRelatedField()
    sans = StringRelatedField()
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
    user = StringRelatedField()
    movie = StringRelatedField()
    class Meta:
        model = Comment
        fields = ['user', 'date','text', 'movie']


class CommentRetrieveUpdateDestroySerializer(ModelSerializer):
    user = StringRelatedField()
    movie = StringRelatedField()
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
    movie = StringRelatedField()
    class Meta:
        model = Criticism
        fields = ['description', 'read_time', 'movie']


class CriticismRetrieveUpdateDestroySerializer(ModelSerializer):
    movie = StringRelatedField()
    class Meta:
        model = Criticism
        fields = ['description', 'read_time', 'movie']