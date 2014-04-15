import urllib2
import wiki_parser
from flask import Flask, url_for, request, render_template, redirect, session, \
        escape, Markup

app = Flask(__name__)
app.secret_key = 'abc123'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/race')
def race():
    wiki_response = urllib2.urlopen('https://en.wikipedia.org/wiki/Cat')
    html = wiki_response.read()
    # html is a bytestring, but everyone expects unicode
    article = wiki_parser.get_article(html.decode('utf-8'));
    return render_template('race.html', start_page = article)

@app.route('/clicks')
def clicks():
    return 'Clicks game'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
