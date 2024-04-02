from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Movie
from .forms import MovieForm, RatingForm

# Create your views here.
def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.user.is_authenticated:
        is_rated = movie.ratings.filter(user_id=request.user).exists()
    else:
        is_rated = False

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.user_id = request.user
            rating.movie_id = movie
            rating.save()

            messages.success(request, 'Rating is added.')
            return redirect('movies:detail', movie.id)
        
        else:
            messages.error(request, 'Rating failed.')

    else:
        form = RatingForm()

    return render(request, 'movies/detail.html', {
        'title': movie.name,
        'movie': movie,
        'form': form,
        'is_rated': is_rated or None
    })

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.created_by = request.user
            movie.save()

            messages.success(request, 'A movie is added.')

            return redirect('/')
        
    else:
        form = MovieForm()
    
    return render(request, 'movies/add.html', {
        'title': 'Add Movie',
        'form': form
    })

@login_required
def edit_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            form.save()

            messages.success(request, 'Details are updated.')
            return redirect('movies:detail', movie.id)
        
        else:
            messages.error(request, 'Update failed!')
        
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/add.html', {
        'title': 'Edit Movie',
        'form': form
    })

@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    movie.delete()

    messages.success(request, 'Movie has been deleted.')

    return redirect('core:home')
    
