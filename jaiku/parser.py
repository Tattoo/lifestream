import urllib
from xml.dom import minidom as xml_parser
from datetime import datetime
from blog.models import Entry
from django.contrib.auth.models import User
import utilities

class Jaiku(utilities.Parser):
    def __init__(self, username, user):
        self.username = username
        self.user = user
        
    def parse(self):
        jaikuUrl = "http://%s.jaiku.com/feed/rss" % (self.username)
        data = self.fetch(jaikuUrl)
        print data
        xmlData = xml_parser.parseString(data)
        
        for node in xmlData.getElementsByTagName('item'):
            title = self.getText(node.getElementsByTagName('title')[0].childNodes)
            url =  self.getText(node.getElementsByTagName('link')[0].childNodes)
            #filter out all other entries such as last.fm
            if (url.find('jaiku') != -1): 
                # once again, make a proper datetime out of the date in the xml
                d = self.getText(node.getElementsByTagName('pubDate')[0].childNodes)
                d = d.split(' ')
                d.pop() # remove the day of the week
                d.pop(0) # remove the time zone
                t = d[3].split(':') # divide time to it's own list
                d.pop() # remove the time 
                months = { 'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12' }
                d[1] = months[d[1]] # correct three-letter month as a number 
            
                #d and t are now string lists, make one int list out of them
                date = [] 
                for i in d:
                    date.append(int(i))
                for j in t:
                    date.append(int(j))
            
                date = datetime(date[2], date[1], date[0], date[3], date[4], date[5])
            
                # check that entry is not yet in database
                a = Entry.objects.filter(name=title, date=date)
                if (len(a) < 1):
                    u = User.objects.filter(username=self.user)[0]
                    entry = Entry(name=title, url=url, date=date, entry_type='jaiku', user=u)
                    entry.save()
