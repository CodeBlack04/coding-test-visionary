from django.shortcuts import render
from django.db.models import Q
from movies.models import Movie
from movies.forms import MovieFilterForm

# Create your views here.
def home(request):
    movies = Movie.objects.all().order_by('-created_at')
    query = request.GET.get('query', '')
    form = MovieFilterForm(request.GET)

    if form.is_valid():
        genre_types = form.cleaned_data['genre_types']
        rating_types = form.cleaned_data['rating_types']

        if genre_types:
            for genre in genre_types:
                movies = movies.filter(genre=genre)
    
        if rating_types:
            for rating in rating_types:
                movies = movies.filter(rating=rating)
            
    if query:
        movies = movies.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'core/home.html', {
        'title': 'Home Page',
        'movies': movies,
        'form': form,
        'query': query
    })
