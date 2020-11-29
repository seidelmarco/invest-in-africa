import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3
from bs4 import BeautifulSoup

test_data = '''
<div class="column column--aside">
     <div class="group group--elements left">
      <div class="element element--list">
       <header class="header header--secondary">
        <h2 class="title">
         <span class="label">
          Key Data
         </span>
        </h2>
       </header>
       <ul class="list list--kv list--col50">
        <li class="kv__item">
         <small class="label">
          Open
         </small>
         <span class="primary">
          $21.89
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Day Range
         </small>
         <span class="primary">
          21.69 - 22.80
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          52 Week Range
         </small>
         <span class="primary">
          3.43 - 26.16
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Market Cap
         </small>
         <span class="primary">
          $2.77B
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Shares Outstanding
         </small>
         <span class="primary">
          126.01M
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Public Float
         </small>
         <span class="primary">
          118.88M
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Beta
         </small>
         <span class="primary">
          1.24
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Rev. per Employee
         </small>
         <span class="primary">
          $191.34K
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          P/E Ratio
         </small>
         <span class="primary is-na">
          N/A
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          EPS
         </small>
         <span class="primary">
          -$1.53
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Yield
         </small>
         <span class="primary">
          0.00%
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Dividend
         </small>
         <span class="primary">
          $0.17
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Ex-Dividend Date
         </small>
         <span class="primary">
          Mar 12, 2020
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Short Interest
         </small>
         <span class="primary">
          66.24M
         </span>
         <span class="secondary">
          10/30/20
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          % of Float Shorted
         </small>
         <span class="primary">
          55.72%
         </span>
         <span class="secondary no-value">
         </span>
        </li>
        <li class="kv__item">
         <small class="label">
          Average Volume
         </small>
         <span class="primary">
          10.08M
         </span>
         <span class="secondary no-value">
         </span>
        </li>
       </ul>
      </div>
     </div>
'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SERVICE_URL = 'https://www.marketwatch.com/investing/stock/'
ticker = input('Enter Tickersymbol: ')

url = input('Enter URL or hit enter if you typed in a Tickersymbol: ')
if len(url) < 1: url = SERVICE_URL + ticker

# die beiden Funktionen sind für eine Variante mit der Library Requests
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


r = urllib.request.urlopen(url, context=ctx).read()    # read return byte obj, decode returns str obj

#save_html(r.content, url)
print(type(r))
print(r[:100])

#html = open_html(url)

print('*********************************')

soup = BeautifulSoup(test_data, 'html.parser')

# for developing and debugging reasons
#print(soup.prettify())

print(soup.title)

listeneintrag_li = soup.li
print(type(listeneintrag_li))
print(listeneintrag_li.name)
print(listeneintrag_li.attrs)

for i in soup.find_all('small'):
    print(i.get_text())
    for c in i:
        print(soup.find_all('span'))
#Keydata als dictionary
kd = dict()

#print(soup.title.string)
#print(soup.title.parent.name)
##print(soup.find_all('li'))
#for link in soup.find_all('a'):
 #   print(link.get('href'))
#print(soup.get_text())

#____Kinds of Objects
'''
Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. But you’ll only ever have to 
deal with about four kinds of objects: Tag, NavigableString, BeautifulSoup, and Comment.
'''

conn = sqlite3.connect('stocks_keydata.sqlite3')
cur = conn.cursor()

cur.executescript('''
                
                CREATE TABLE IF NOT EXISTS Keydata (
                id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
                name    TEXT UNIQUE,
                ticker  TEXT UNIQUE,
                peratio FLOAT,
                dividend FLOAT,
                eps     FLOAT,
                yield   FLOAT
                );
''')



