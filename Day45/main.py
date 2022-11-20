##SCRAP A STATIC SITE
# from bs4 import BeautifulSoup
#
# with open('website.html', mode='r', encoding="utf8") as file:
#     content = file.read()
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.name)
# print(soup.title.string)


##show html as it is
# print(soup.prettify())


## first a tag
# print(soup.a)


## find all a tags
# print(soup.findAll(name='a'))


## iterate in anchor tags
# for tag in soup.findAll(name='a'):
##get text
# print(tag.getText())
##or
# print(tag.text)
## get link
# print(tag.get('href'))

## find particular tag in html with id
# print(soup.find(name='h1', id='name'))
## find particular tag in html with class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
# print(section_heading.name)
# print(section_heading.get("class"))
##select by nested html tag
# h3_heading = soup.select_one(selector="p a")
# print(h3_heading)
# name = soup.select_one(selector="#name")
# print(name)
##find add heading class
# print(soup.select(selector=".heading"))


## SCRAP A LIVE WEBSITE

from bs4 import BeautifulSoup
import requests

SITE = "https://news.ycombinator.com/news"
response = requests.get(SITE)
soup = BeautifulSoup(response.text, "html.parser")
a_tags = soup.select(selector=".titleline>a")
article_text = []
article_link = []
for tag in a_tags:
    article_text.append(tag.getText())
    article_link.append(tag.get("href"))
article_upvotes = [int(tag.getText().split(' ')[0]) for tag in soup.select(selector='.subline .score')]
highest_index = article_upvotes.index(max(article_upvotes))
print(article_text[highest_index])
print(article_link[highest_index])
print(article_upvotes[highest_index])
