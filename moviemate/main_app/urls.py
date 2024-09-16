from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movie_index, name='movie_index'),
  path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
  path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
  path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
  path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
  path('movies/<int:movie_id>/add_watch/', views.add_watch, name='add_watch'),
  path('ratings/create/', views.RatingCreate.as_view(), name='rating_create'),
  path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='rating_detail'),
  path('ratings/', views.RatingList.as_view(), name='rating_index'),
  path('ratings/<int:pk>/update/', views.RatingUpdate.as_view(), name='rating_update'),
  path('ratings/<int:pk>/delete/', views.RatingDelete.as_view(), name='rating_delete'),
  path('movies/<int:movie_id>/associate_rating/<int:rating_id>/', views.associate_rating, name='associate_rating'),
  path('movies/<int:movie_id>/remove_rating/<int:rating_id>/', views.remove_rating, name='remove_rating'),
]