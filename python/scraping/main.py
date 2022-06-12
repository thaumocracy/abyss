import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')


soup = BeautifulSoup(response.text, 'html.parser')
scores = soup.select('.score')
things = soup.select('.athing')


def sort_top_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'])


def getLinks(things, id):
    for thing in things:
        if(thing.get('id') == id):
            link = thing.select('a.storylink')
            return link


def make_links_list(scores, things):
    massive = []
    for score in scores:
        item = (score.getText().split(' '))
        if int(item[0]) > 100:
            found = score.get('id')[6:]
            links = getLinks(things, found)
            for link in links:
                massive.append({
                    "link": link.get('href', None),
                    "title": link.getText(),
                    "votes": item[0]
                })
    return massive


print(sort_top_stories(make_links_list(scores, things)))
