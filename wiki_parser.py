import urllib2
from bs4 import BeautifulSoup

def get_article(html):
    parsed_html = BeautifulSoup(html)

    # grab the styles
    style_tags = parsed_html.head.find_all(['link', 'style'])
    styles = '\n'.join(unicode(t) for t in style_tags)

    # get the article title
    title = parsed_html.body.find('h1', attrs={'id':'firstHeading'})

    article = parsed_html.body.find('div', attrs={'id':'bodyContent'})

    return unicode(styles) + unicode(title) + unicode(article)
