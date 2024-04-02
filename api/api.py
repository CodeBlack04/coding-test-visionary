from django.http import JsonResponse

from userauth.models import User
from movies.models import Movie, Rating
from .serializers import UserListSerializer, MovieListSerializer, RatingListSerializer

def user_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)

    return JsonResponse({
        'User Json': serializer.data
    })

def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)

    return JsonResponse({
        'Movie Json': serializer.data
    })

def rating_list(request):
    ratings = Rating.objects.all()
    serializer = RatingListSerializer(ratings, many=True)

    return JsonResponse({
        'Ratings json': serializer.data
    })