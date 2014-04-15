import urllib2
from bs4 import BeautifulSoup

def get_article(html):
    parsed_html = BeautifulSoup(html)
    article = parsed_html.body.find('div', attrs={'id':'bodyContent'})
    return unicode(parsed_html.head) + unicode(article)
