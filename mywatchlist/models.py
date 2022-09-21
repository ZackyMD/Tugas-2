from django.db import models

# Create your models here.

class BarangMyWatchlist(models.Model):
    watchedFilm = models.CharField(max_length=50)
    titleWatched = models.TextField()
    ratingWatched = models.TextField()
    releaseDateWatched = models.TextField()
    reviewWatched = models.TextField()
    
