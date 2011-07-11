import urllib
from xml.dom import minidom as xml_parser
from django.db import models

class Parser(object):
    
    def getText(self, nodelist):
        response = ""
        for n in nodelist:
            if (n.nodeType == n.TEXT_NODE):
                response = response + n.data
        return response        

    def fetch(self, url):
        u = urllib.FancyURLopener(None)
        usock = u.open(url)
        rawdata = usock.read()
        usock.close()
        return rawdata
        