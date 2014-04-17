import urllib2
import wiki_parser
import re
from flask import Flask, url_for, request, render_template, redirect, session, \
        escape, Markup

app = Flask(__name__)
app.secret_key = 'abc123'
app.debug = True

wiki_url = 'https://en.wikipedia.org/wiki/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/race')
def race():
    return render_template('race.html', start = 'Cat', end = 'Dog')

@app.route('/clicks')
def clicks():
    return 'clicks game'

@app.route('/wiki/<page>')
def wiki(page):
    wiki_response = urllib2.urlopen(wiki_url + page)
    html = wiki_response.read()
    # html is a bytestring, but everyone expects unicode
    return wiki_parser.get_article(html.decode('utf-8'));

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
