from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from userauth.models import User

import uuid
# Create your models here.
class GenreType(models.TextChoices):
    COMEDY = 'comedy', 'Comedy'
    ACTION = 'action', 'Action'
    CRIME = 'crime', 'Crime'

class RatingType(models.TextChoices):
    PG = 'pg', 'PG'
    R = 'r', 'R'

class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=10, choices=GenreType.choices)
    rating = models.CharField(max_length=10, choices=RatingType.choices)
    release_date = models.DateField()

    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='movies', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        ratings = self.ratings.all()

        if not ratings:
            return None
        
        total = sum(rating.rating for rating in ratings)
        count = ratings.count()

        return round(total/count, 2)

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user_id = models.ForeignKey(User, related_name='ratings', blank=True, null=True, on_delete=models.SET_NULL)
    movie_id = models.ForeignKey(Movie, related_name='ratings', blank=True, null=True, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user_id.name}-{self.rating}-{self.movie_id.name}'

