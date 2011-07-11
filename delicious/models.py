from django.db import models
import utilities
class DeliciousEntry(models.Model):
    class Admin:
        pass
#    class Meta:                
#        ordering = ["date"]
    description = models.CharField(max_length=200)
    url = models.URLField()
    date = models.DateTimeField()
