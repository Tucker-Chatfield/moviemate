from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Rating
from .forms import WatchesForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movie_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  ratings_movie_doesnt_have = Rating.objects.exclude(id__in = movie.ratings.all().values_list('id'))
  watches_form = WatchesForm()
  return render(request, 'movies/detail.html', {
    'movie': movie, 
    'watches_form': watches_form, 
    'ratings': ratings_movie_doesnt_have
    })

def add_watch(request, movie_id):
  form = WatchesForm(request.POST)
  if form.is_valid():
    new_watch = form.save(commit=False)
    new_watch.movie_id = movie_id
    new_watch.save()
  return redirect('movie_detail', movie_id=movie_id)

def associate_rating(request, movie_id, rating_id):
  Movie.objects.get(id=movie_id).ratings.add(rating_id)
  return redirect('movie_detail', movie_id=movie_id)

def remove_rating(request, movie_id, rating_id):
  Movie.objects.get(id=movie_id)
  Rating.objects.get(id=rating_id)
  Movie.objects.get(id=movie_id).ratings.remove(rating_id)
  return redirect('movie_detail', movie_id=movie_id)

class MovieCreate(CreateView):
  model = Movie
  fields = ['name', 'genre', 'description', 'release']
  success_url = '/movies/'
  
class MovieUpdate(UpdateView):
  model = Movie
  fields = ['genre', 'description', 'release']
  
class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'
  
class RatingCreate(CreateView):
  model = Rating
  fields = '__all__'
  
class RatingList(ListView):
  model = Rating
  
class RatingDetail(DetailView):
  model = Rating
  
class RatingUpdate(UpdateView):
  model = Rating
  fields = ['name', 'color']
  
class RatingDelete(DeleteView):
  model = Rating
  success_url = '/ratings/'