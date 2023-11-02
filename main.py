from bs4 import BeautifulSoup
from requests import get

article_texts = []
article_links = []

# get the html doc
response = get('https://news.ycombinator.com')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='tr', class_='athing')
upvotes = soup.find_all(name='span', class_='score')

# prepare upvotes for processing
for n in range(len(upvotes)):
    upvotes[n] = upvotes[n].getText()
    vote_num = upvotes[n].split(' ')
    upvotes[n] = int(vote_num[0])

# get headlines and links
for article_tag in articles:
    article = article_tag.find(name='span', class_='titleline')
    text = article.getText()
    article_texts.append(text)
    links = [a.get('href') for a in article.select('a')]
    article_links.append(links[0])

# find the #1 article and print
high_score = max(upvotes)
index = upvotes.index(high_score)
print(f'The most upvoted article is "{article_texts[index]}", {article_links[index]} with {high_score} upvotes!')
