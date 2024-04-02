from django.urls import path

from . import api

app_name = 'api'

urlpatterns = [
    path('users/', api.user_list, name='api-user-list'),

    path('movies/', api.movie_list, name='api-movie-list'),

    path('ratings/', api.rating_list, name='api-rating-list'),
]