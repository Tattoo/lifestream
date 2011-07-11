from django.db import models
import utilities

class JaikuEntry(models.Model):
    class Admin:
        pass
 #   class Meta:                
 #       ordering = ["date"]
    title = models.CharField(max_length=200)
    url = models.URLField()
    date = models.DateTimeField()
