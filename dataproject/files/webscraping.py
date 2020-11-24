from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

count = int(input('Enter count: '))
pos = int(input('Enter position: '))

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req, context=ctx).read()
soup = BeautifulSoup(webpage, 'html.parser')        #hier bekommst du den ganzen Eintopf als object
print(type(soup))


# Retrieve all ... a tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

for c in range(count):

    tagpos = tags[pos-1]
    print('Retrieving:', tagpos.get('href', None))
    tagpos_url = tagpos.get('href', None)

    req = Request(tagpos_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    #for tag in tags:
        #print(tag.get('href', None))

# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
    #print('URL: ', tag.get('href="https://www.caledoniamining.com/investors/regulatory-news-alerts/"', None))
    #print('URL: ', tag.get('https://www.caledoniamining.com/investors/key-financials/', None))
    #print('Contents: ', tag.contents[0])

#print(soup.prettify())

print(soup.get_text())



