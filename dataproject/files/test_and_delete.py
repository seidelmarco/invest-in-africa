import requests
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

# Constructing the special URL

SERVICE_URL = 'https://www.marketwatch.com/investing/stock/'
ticker = input('Enter Tickersymbol: ')

url = input('Enter URL or hit enter if you typed in a Tickersymbol: ')
if len(url) < 1: url = SERVICE_URL + ticker

'''
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
'''


def save_html(html, path):      # path ist file_name, html ist die response als html bytes object
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):                # path ist file_name
    with open(path, 'rb') as f:
        return f.read()


# Making the request
response = requests.get(url)

print(response.content[:100])

save_html(response.content, 'html_object_locally')

html = open_html('html_object_locally')

print(html[:200])
print(type(html))


# scraping mit BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# for developing and debugging reasons
#print(soup.prettify())

print(soup.title.contents)

listeneintrag_li = soup.li
print(type(listeneintrag_li))
print(listeneintrag_li.name)
print(listeneintrag_li.attrs)

#count = 0
#for i in soup.find_all('small'):
 #   print(i.get_text())
  #  count += 1

   # print(soup.select('.label'))    # . returns class=attr
    #print(soup.select('.primary'))

    #if count > 0: break

for i in soup.select('.label') and soup.select('.primary'):
    print(i.get_text())
    peratio = None

'''
<li class="kv__item">
                    <small class="label">52 Week Range</small>
                    <span class="primary ">6.51 - 29.39</span>
                    <span class="secondary no-value"></span>
                </li>
                <li class="kv__item">
                    <small class="label">Market Cap</small>
                    <span class="primary ">$181.3M</span>
                    <span class="secondary no-value"></span>
                </li>
                <li class="kv__item">
                    <small class="label">Shares Outstanding</small>
                    <span class="primary ">12.12M</span>
                    <span class="secondary no-value"></span>
                </li>
'''

rows = soup.select('.kv__item')
print(rows)
print(type(rows))       #siehe: <class 'bs4.element.ResultSet'> AttributeError: ResultSet object has no attribute 'children'.


for i in range(len(rows)):
    print(i, rows[i])

print('*************************')

# A string corresponds to a bit of text within a tag.
# Beautiful Soup uses the NavigableString class to contain these bits of text:

soup2 = BeautifulSoup('<small class="label">Shares Outstanding</small>', 'html.parser')
tag = soup2.small
print(type(tag.string), tag.string)

# Convert NavigableString into String
small_unicode_string = str(tag.string)
print(type(small_unicode_string), small_unicode_string)

'''
WICHTIG!
NavigableString supports most of the features described in Navigating the tree and Searching the tree, but not all of 
them. In particular, since a string can’t contain anything (the way a tag may contain a string or another tag), 
strings don’t support the .contents or .string attributes, or the find() method.

If you want to use a NavigableString outside of Beautiful Soup, you should call unicode() on it to turn it into 
a normal Python Unicode string. If you don’t, your string will carry around a reference to the entire 
Beautiful Soup parse tree, even when you’re done using Beautiful Soup. This is a big waste of memory.
'''

#BeautifulSoup
'''
The BeautifulSoup object represents the parsed document as a whole. For most purposes, 
you can treat it as a Tag object.
This means it supports most of the methods described in Navigating the tree and Searching the tree.
'''

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document>", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
rep = doc.find(text="INSERT FOOTER HERE").replace_with(footer)

print(doc)
print(soup.name)


# .contents and .children

li_tag = soup.li            #findet den zweiten (!) li-Tag in ul in Zeile 377 (html_object_locally) WARUM???
print(li_tag.contents)

for child in li_tag.children:
    a_tag = child
    for next_child in a_tag:
        print(type(next_child), next_child)
        str_next_child = str(next_child)

print('*+*+'*10)
print('.parents')
li_tag = soup.li
print('Es wird nur der erste li Link gefunden.', li_tag)
for parent in li_tag.parents:
    print('Parent name:', parent.name)

div_tag = soup.find_all('div')
print(div_tag)
