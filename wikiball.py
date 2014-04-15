import urllib2
import re
from time import time
from flask import Flask, url_for, request, render_template, redirect, session, \
        escape
app = Flask(__name__)

app.secret_key = 'abc123'
app.debug = True

@app.route('/start',methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['start'] = request.form['start']
        session['end'] = request.form['end']
        session['click'] = 0
        session['sTime'] = time() 
        wiki_response = urllib2.urlopen('https://en.wikipedia.org/wiki/' + session['start'])
        return wiki_response.read()
    return '''
           <form action="" method="post">
               <p>Start<input type=text name=start>
               <p>End<input type=text name=end>
               <p>Name<input type=text name=username>
               <p><input type=submit value=Login>
           </form>
       '''
@app.route('/')
def index(done = None):
    if done :
        return  render_template('index.html', clicks=str(session['click']),time=str(session['eTime']))
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

@app.route('/<path:path>')
def catch_all(path):
    session['click'] += 1
    #check to see if we are done
    match = re.match('.*\/(.*)',path)
    if match:
        if match.group(1) == session['end'] :
            session['eTime'] = time() - session['sTime']
            boolean = True
            return render_template('index.html',time=session['eTime'],clicks=session['click'])
    wiki_response = urllib2.urlopen('https://en.wikipedia.org/' + path)
    html = wiki_response.read()
    return html

if __name__ == '__main__':
    app.run()
