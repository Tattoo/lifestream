from django.contrib import admin
from lifestream.jaiku.models import JaikuEntry

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(JaikuEntry, AuthorAdmin)