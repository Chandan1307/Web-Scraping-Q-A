'''
What is web scrapping?
The technique of taking the html file sent by the server into python and scrapping it instead of giving it to the browser and displaying it is called Web scrapping.

Two ways of getting data from a website:
1) Using API
2) HTML web scrapping using some tool like bs4
'''
'''
# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib
'''

import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)  # r variable has all the HTML Code
htmlContent = r.content  # r return response so if we want the code we write r.content
# print(htmlContent)  # printing the code

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal

# Commonly used types of objects:

# Get the title of the HTML page
title = soup.title
# print(type(title))  # 1. tag

# print(type(title.string))  # 2. NavigableString00

# print(type(soup))   # 3. BeautifulSoup

# 4. Comment
markup = '<p><!--this is a comment--></p>'
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)


# Get classes of any element in the HTML Page
print(soup.find('p')['class'])


# Find all the elements with class lead
print(soup.find_all('p', class_='lead'))


# Get the text from the tags/soup
print(soup.find('p').get_text())


# Get the all soup
print(soup.get_text())


# Get all the Anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText)


navbarSupportedContent = soup.find(id='navbarSupportedContent')
# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)

# elem = soup.select('#loginModal')[0] 
# print(elem)