from django.db import models
import utilities
# Create your models here.

class LastFmEntry(models.Model):
    class Admin:
        pass
#    class Meta:                
#        ordering = ["date"]
    artist = models.CharField(max_length=200)
    track = models.CharField(max_length=200, unique_for_date="date")
    album = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    image = models.URLField(blank=True)
    date = models.DateTimeField()
    
