import urllib2
from bs4 import BeautifulSoup

def get_article(html):
    parsed_html = BeautifulSoup(html)

    # grab the styles
    styles = '\n'.join(parsed_html.head.find_all(['link', 'style']))

    # get the article title
    title = parsed_html.body.find('h1', attrs={'id':'firstHeading'})

    article = parsed_html.body.find('div', attrs={'id':'bodyContent'})
    # get rid of external links
    article.find('div', attrs={'class':'reflist'}).decompose()

    return unicode(styles) + unicode(title) + unicode(article)
