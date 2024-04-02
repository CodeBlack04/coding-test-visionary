from rest_framework import serializers
from userauth.models import User
from movies.models import Movie, Rating

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'phone',
            'password',
            'email',
        )

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'genre',
            'rating',
            'release_date',
        )

class RatingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'user_id',
            'movie_id',
            'rating',
        )