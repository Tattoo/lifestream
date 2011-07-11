from django.db import models
from django.contrib.auth.models import User

ENTRY_TYPES = (
    ('lastfm', 'Last.fm'),
    ('delicious', 'Delicious'),
    ('jaiku', 'Jaiku')
)

class Entry(models.Model):
    class Admin:
        pass
    class Meta:
        ordering = ["date"]
       
    user = models.ForeignKey(User)
    entry_type = models.CharField(choices=ENTRY_TYPES, max_length=10)
    url = models.URLField(blank=True)
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    
    #Delicious specific
    description = models.CharField(max_length=200, blank=True)
    
    #Last.fm specific
    artist = models.CharField(max_length=200, blank=True)
    album = models.CharField(max_length=200, blank=True)
    image = models.URLField(blank=True)


class LoginCredentials(models.Model):
        class Admin:
            pass
            
        user = models.ForeignKey(User)
        service_type = models.CharField(choices=ENTRY_TYPES, max_length=10)
        username = models.CharField(max_length=200)
        password = models.CharField(max_length=100, blank=True)