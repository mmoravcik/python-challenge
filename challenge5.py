# www.pythonchallenge.com/pc/def/peak.html

from cStringIO import StringIO
import urllib2
import pickle # peak hell

def get_web_content(url):
   get = urllib2.urlopen(url)
   return get.read()

src = StringIO()
source = get_web_content('http://www.pythonchallenge.com/pc/def/banner.p')
dst = StringIO(source)

data = pickle.load(dst)

for line in data:
    output = ""
    for letter_info in line:
        for counter in range(0, letter_info[1]):
            output += letter_info[0]
    print output

