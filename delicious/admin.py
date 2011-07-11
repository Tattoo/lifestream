from django.contrib import admin
from lifestream.delicious.models import DeliciousEntry

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(DeliciousEntry, AuthorAdmin)