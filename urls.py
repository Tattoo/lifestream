from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from blog.views import *

urlpatterns = patterns('',
    # Example:
    # (r'^lifestream/', include('lifestream.foo.urls')),
    (r'^/?$', index),
    (r'^lifestream/?$', index),
    (r'^lifestream/show/(?P<username>\w{1,30})/?$', show), # usernames are max. 30 letters in Django
    (r'^lifestream/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './blog/static'}),
    

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),
)
