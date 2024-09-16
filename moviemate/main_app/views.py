from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Rating
from .forms import WatchesForm

def about(request):
  return render(request, 'about.html')

@login_required
def movie_index(request):
  movies = Movie.objects.filter(user=request.user)
  return render(request, 'movies/index.html', {'movies': movies})

@login_required
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

@login_required
def associate_rating(request, movie_id, rating_id):
  Movie.objects.get(id=movie_id).ratings.add(rating_id)
  return redirect('movie_detail', movie_id=movie_id)

@login_required
def remove_rating(request, movie_id, rating_id):
  Movie.objects.get(id=movie_id)
  Rating.objects.get(id=rating_id)
  Movie.objects.get(id=movie_id).ratings.remove(rating_id)
  return redirect('movie_detail', movie_id=movie_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('movie_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)  
    
class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = ['name', 'genre', 'description', 'release']
  success_url = '/movies/'
  
  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
  
class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = ['genre', 'description', 'release']
  
class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'
  
class RatingCreate(LoginRequiredMixin, CreateView):
  model = Rating
  fields = '__all__'
  
class RatingList(LoginRequiredMixin, ListView):
  model = Rating
  
class RatingDetail(LoginRequiredMixin, DetailView):
  model = Rating
  
class RatingUpdate(LoginRequiredMixin, UpdateView):
  model = Rating
  fields = ['name', 'color']
  
class RatingDelete(LoginRequiredMixin, DeleteView):
  model = Rating
  success_url = '/ratings/'
  
class Home(LoginView):
  template_name = 'home.html'