import urllib2
from bs4 import BeautifulSoup

def get_article(html):
    parsed_html = BeautifulSoup(html)
    title = parsed_html.body.find('h1', attrs={'id':'firstHeading'})
    article = parsed_html.body.find('div', attrs={'id':'bodyContent'})
    return unicode(parsed_html.head) + unicode(title) + unicode(article)
