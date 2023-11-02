from bs4 import BeautifulSoup
from requests import get

article_texts = []
article_links = []
article_upvotes = []
upvotes = []

# get the html doc
response = get('https://news.ycombinator.com')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='tr', class_='athing')
subtexts = soup.find_all(name='td', class_='subtext')

# check if article has upvotes
for subtext in subtexts:
    score = subtext.find(name='span', class_='score')
    if subtext.find(name='span', class_='score'):
        upvotes.append(score)
    else:
        upvotes.append('test')

# prepare upvotes for processing
for upvote in upvotes:
    if upvote != 'test':
        upvote = upvote.getText()
        vote_num = upvote.split(' ')
        upvote = int(vote_num[0])
        article_upvotes.append(upvote)
    else:
        upvote = 0
        article_upvotes.append(upvote)

# get headlines and links
for article_tag in articles:
    article = article_tag.find(name='span', class_='titleline')
    text = article.getText()
    article_texts.append(text)
    links = [a.get('href') for a in article.select('a')]
    article_links.append(links[0])

# find the #1 article and print
high_score = max(article_upvotes)
index = article_upvotes.index(high_score)
print(f'The most upvoted article is "{article_texts[index]}", {article_links[index]} with {high_score} upvotes!')
