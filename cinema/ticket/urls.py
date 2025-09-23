from django.urls import path
from ticket.views import *



urlpatterns = [
    path('cinema-list-create', CinemaListCreate.as_view()),
    path('cinema-retrieve-update-destroy/<str:pk>', CinemaRetrieveUpdateDestroy.as_view()),
    path('movie-list-create', MovieListCreate.as_view()),
    path('movie-retrieve-update-destroy/<str:pk>', MovieRetrieveUpdateDestroy.as_view()),
    path('sans-list-create', SansListCreate.as_view()),
    path('sans-retrieve-update-destroy/<str:pk>', SansRetrieveUpdateDestroy.as_view()),
    path('list-create', TicketListCreate.as_view()),
    path('retrieve-update-destroy/<str:pk>', TicketRetrieveUpdateDestroy.as_view()),
    path('actor-list-create', ActorListCreate.as_view()),
    path('actor-retrieve-update-destroy/<str:pk>', ActorRetrieveUpdateDestroy.as_view()),
    path('comment-list-create', CommentListCreate.as_view()),
    path('comment-retrieve-update-destroy/<str:pk>', CommentRetrieveUpdateDestroy.as_view()),
    path('genre-list-create', GenreListCreate.as_view()),
    path('genre-retrieve-update-destroy/<str:pk>', GenreRetrieveUpdateDestroy.as_view()),
    path('criticism-list-create', CriticismListCreate.as_view()),
    path('criticism-retrieve-update-destroy/<str:pk>', CriticismRetrieveUpdateDestroy.as_view()),
]