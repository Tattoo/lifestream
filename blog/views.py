from django.contrib.auth.models import User
from django.http import HttpResponse    
from django.template import Context, loader

from lastfm import parser as lastFmParser
from delicious import parser as deliciousParser
from jaiku import parser as jaikuParser


from blog.models import Entry, LoginCredentials

def index(req):
    t = loader.get_template('index.html')

#    lfm = lastFmParser.LastFm('Tattoo_', 'aaa')
#    lfm.parse()
#    d = deliciousParser.Delicious('Tattoo__', 'larry-', 'aaa')
#    d.parse()
#    j = jaikuParser.Jaiku('wuname', 'aaa')
#    j.parse()
    
#    fb =  facebookParser.Facebook('610943679')
#    fb.parse()

    users = User.objects.all()
    entries = []
    for u in users:
        entries.append({'username': u.username, 'entries': Entry.objects.filter(user=u).order_by('-date')})

    c = Context({
        'entriesByUsers' : entries
    })
    return HttpResponse(t.render(c))
    
def show(req, username):
    t = loader.get_template('show.html')
    u = User.objects.filter(username=username)
    if (len(u) > 1):
        raise Http404
    else: 
        u = u[0]
        c = Context({
            'username': username,
            'entries': Entry.objects.filter(user=u).order_by('-date')
        })
        return HttpResponse(t.render(c))
        
    