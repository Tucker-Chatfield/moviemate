from django.db import models
from django.urls import reverse

TIMES = (
  ('F', 'First'),
  ('S', 'Second'),
  ('E', 'Extra')
)

class Rating(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("rating_detail", kwargs={"pk": self.id})
  
class Movie(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release = models.IntegerField()
  ratings = models.ManyToManyField(Rating)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("movie_detail", kwargs={"movie_id": self.id})

class Watches(models.Model):
  date = models.DateField('Watch date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
    )
  
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
    
  