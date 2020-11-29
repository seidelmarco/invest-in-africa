from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# scraping mit BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# for developing and debugging reasons
print(soup.prettify())

print(soup.title.contents)

# A string corresponds to a bit of text within a tag.
# Beautiful Soup uses the NavigableString class to contain these bits of text:

soup2 = BeautifulSoup('<small class="label">Shares Outstanding</small>', 'html.parser')
small_tag = soup2.small
print(type(small_tag.string), small_tag.string)

# Convert NavigableString into String
small_unicode_string = str(small_tag.string)
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

# Navigating the Tree

# Using a tag name as an attribute will give you only the first tag by that name:
print(soup.body.b)    # reinzoomen indem man sich an den Tagnamen entlanghangelt

print(soup.find_all('a')[1])

# .contents and .children
# A tag’s children are available in a list called .contents:

head_tag = soup.head
print(head_tag)
print(head_tag.contents)

p_tag = soup.p
print(p_tag.contents)

#Instead of getting them as a list, you can iterate over a tag’s children using the .children generator:
for child in p_tag.children:
    b_tag = child
    for next_child in b_tag:
        print(type(next_child), next_child)
        str_next_child = str(next_child)

# .descendants

# auch das geht wieder nur für einen Tag und NICHT mit find_all! You treated a list of elements like a single elem.

print(head_tag.contents)

head_tag = soup.head

count = 0
for child in head_tag.descendants:
    count += 1
    print(count,'. Schleife:')
    print('Kompletter Head-Tag:')
    print(head_tag)
    print('Head-Tag hat zwei Nachkommen:')
    print(child)

# .string
print('*+*+'*10)
title_tag = soup.title
print(title_tag.string)

# .strings and stripped_strings
# If there’s more than one thing inside a tag, you can still look at just the strings. Use the .strings generator:

for string in soup.strings:
    print(repr(string))
    '\n'

for string in soup.stripped_strings:
    print(repr(string))

# Going up
# Continuing the “family tree” analogy, every tag and every string has a parent: the tag that contains it.
#
# .parent

print('*+*+'*10)
title_tag = soup.title
print('Title tag:', title_tag)
print('Parent:', title_tag.parent)

# .parents

# You can iterate over all of an element’s parents with .parents. This example uses .parents to travel
# from an <a> tag buried deep within the document, to the very top of the document:
print('*+*+'*10)
print('.parents')
link = soup.a
print('Es wird nur der erste Link gefunden.', link)
for parent in link.parents:
    print('Parent name:', parent.name)


# Going sideways
print('*+*+'*10)
print('Going sideways:')
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
print(sibling_soup.prettify())

# .next_sibling and .previous_sibling
print('*+*+'*10)
print('.next_sibling and .previous_sibling')
print('*+*+'*10)
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

print('''
Okay! Wir können jetzt runter und hoch gehen
Tags direkt ansprechen
zu .children und .parents gehen
zu .next_sibling and .previous_sibling gehen
vor und zurück
aber wie wählen wir EIN Kind, einen Tag unter vielen aus??? Wenn es alles mehrmals gibt???
''')

# In real documents, the .next_sibling or .previous_sibling of a tag will usually be a string containing whitespace.
# Going back to the “three sisters” document:
# You might think that the .next_sibling of the first <a> tag would be the second <a> tag. But actually, it’s a string:
# the comma and newline that separate the first <a> tag from the second:

link = soup.a
print(link)
print('Das Komma und ein Linefeed ist das Geschwister:', link.next_sibling)
comma = link.next_sibling
print('Nach dem Komma kommt das nächste Geschwister:', comma.next_sibling)

# .next_siblings and .previous_siblings
# You can iterate over a tag’s siblings with .next_siblings or .previous_siblings:

for sibling in soup.a.next_siblings:
    print(repr(sibling))

for sibling in soup.find(id="link3").previous_siblings:  # ids sind am besten; damit kann man direkt ansprechen
    print(repr(sibling))

# Going back and forth - the next and previous element
print('*+*+'*10)
print('Going back and forth')
print('*+*+'*10)
print('''Here’s the final <a> tag in the “three sisters” document. Its .next_sibling is a string: the conclusion of 
the sentence hat was interrupted by the start of the <a> tag.:''')
last_a_tag = soup.find("a", id="link3")
print(last_a_tag)

print('Nächster Geschwister:', last_a_tag.next_sibling)
print('Nächstes Element:', last_a_tag.next_element, ' - das ist wichtig, um die Values der Tags zu finden.')

print('use these iterators to move forward or backward in the document as it was parsed')
print('.next_elements and .previous_elements')
for element in last_a_tag.next_elements:
    print(repr(element))

# Searching the tree
print('*+*+'*10)
print('Searching the tree')
print('*+*+'*10)

