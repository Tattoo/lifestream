import urllib
import utilities
from xml.dom import minidom as xml_parser
from datetime import datetime 
from blog.models import Entry
from django.contrib.auth.models import User

class Delicious(utilities.Parser):
    def __init__(self, username, password, user):
        self.username = username
        self.password = password
        self.user = user
    
    def parse(self):
        url =  "https://%s:%s@api.del.icio.us/v1/posts/recent" % (self.username, self.password)
        xmlData = xml_parser.parseString(self.fetch(url))
        
        for node in xmlData.getElementsByTagName('post'):
            description = node.getAttribute('description')
            url = node.getAttribute('href')
            temp = node.getAttribute('time')
            temp = temp.split('T')
            d = temp[0].split('-')
            t = temp[1].split(':')
            t[2] = t[2].strip('Z')

            date = []
            for i in d:
                date.append(int(i))
            for j in t:
                date.append(int(j))
    
            acceptable = datetime(date[0], date[1], date[2], date[3], date[4], date[5])

            a = Entry.objects.filter(name=url, date=acceptable)
            if(len(a) < 1):
                u = User.objects.filter(username=self.user)[0]
                entry = Entry(name=url, description=description, date=acceptable, entry_type='delicious', user=u)
                entry.save()
        