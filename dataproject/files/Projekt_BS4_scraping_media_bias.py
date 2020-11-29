# https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/

from bs4 import BeautifulSoup
import requests

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

response = requests.get(url)

print(response.content[:100])


def save_html(html, path):          #path ist filename
    with open(path, 'wb') as f:
        f.write(html)


save_html(response.content, 'media_bias_locally')


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


html = open_html('media_bias_locally')


soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify()[:50000])