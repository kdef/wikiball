import urllib2
from flask import Flask, url_for, request, render_template, redirect, session, \
        escape

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
    # need to process the html here then throw it in a template
    # return render_template('race.html', start_page = html)
    return html

@app.route('/clicks')
def clicks():
    return 'Clicks game'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
