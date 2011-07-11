from lifestream.blog.models import Entry
from django.contrib.auth.models import User
from datetime import datetime 
from xml.dom import minidom as xml_parser

import urllib 
import utilities

class LastFm(utilities.Parser):
    def __init__(self, username, user):
        self.username = username
        self.api_key = '8e354c231a6864b45d741de3816cfebf'
        self.method = 'user.getrecenttracks'
        self.user = user
        
    def handleImageUrls(self, nodelist):
        res = []
        for n in nodelist:
            if(n.getAttribute('size') == 'medium'):
                res.append(n)
        return res
    
    def parse(self, **params):
        url = 'http://ws.audioscrobbler.com/2.0/?method=%s&user=%s&api_key=%s' % (self.method, self.username, self.api_key)
        # run it through xml parser to get it under DOM and therefore under manipulation
        xmlData = xml_parser.parseString(self.fetch(url)) 
        
        for node in xmlData.getElementsByTagName('track'):
            artistName = self.getText(node.getElementsByTagName('artist')[0].childNodes)
            trackName = self.getText(node.getElementsByTagName('name')[0].childNodes)
            albumName = self.getText(node.getElementsByTagName('album')[0].childNodes)
            urlToTrack = self.getText(node.getElementsByTagName('url')[0].childNodes)
            urlToImage =  self.getText(self.handleImageUrls(node.getElementsByTagName('image'))[0].childNodes)
                        
            # parse a valid datetime-object out of the (quite valid :( ) date string gotten from the xml
            dateOfEntry = self.getText(node.getElementsByTagName('date')[0].childNodes)
            # split date and time from the string
            d = dateOfEntry.split(',')
            
            # split date into YEAR, MONTH, DATE
            d1 = d[0].split(' ')
            
            # split time into HOURS, MINUTES
            t1 = d[1].split(':')
            
            # Change three-letter month to a number. 
            # Then change the strings in the list (representing numbers) to integers, stripping trailing & leading whitespaces away
            # This way we get something datetime accepts and a valid datetime object for the database
            months = { 'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12' }
            d1[1] = months[d1[1]] 
             
            date = []
            time = []
            
            for i in d1:
                i.strip()
                date.append(int(i))
            for j in t1:
                j.strip()
                time.append(int(j))
                
            constructedDate = datetime(date[2], date[1], date[0], time[0], time[1])
            
            # check that object is in the database already
            a = Entry.objects.filter(name=trackName, date=constructedDate)
            if (len(a) < 1):
                u = User.objects.filter(username=self.user)[0]
                entry = Entry(artist=artistName, name=trackName, album=albumName, url=urlToTrack, image=urlToImage, date=constructedDate, entry_type="lastfm", user=u)
                entry.save()
