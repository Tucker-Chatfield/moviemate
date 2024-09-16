from django.contrib import admin
from .models import Movie, Watches, Rating

admin.site.register(Movie)
admin.site.register(Watches)
admin.site.register(Rating)