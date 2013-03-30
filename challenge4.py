import urllib2
import re

def get_web_content(url):
   get = urllib2.urlopen(url)
   return get.read()


def get_next_url(content):
     match = re.search("[0-9]+", content)
     if match:
         m = match.group()
         return "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % m
     return None

content = "37278"

while True:
    next_url = get_next_url(content)
    if next_url:
        content = get_web_content(next_url)
        print content
    else:
        break;
     

