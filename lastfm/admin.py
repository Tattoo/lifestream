from django.contrib import admin
from lifestream.lastfm.models import LastFmEntry

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(LastFmEntry, AuthorAdmin)