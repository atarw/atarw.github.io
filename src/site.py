import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask (__name__)
app.config.from_object (__name__)

pages = FlatPages (app)
freezer = Freezer (app)

PROJECT_TAG = 'project'

@app.route ('/')
def index ():
	posts = [p for p in pages if PROJECT_TAG not in p ['tags']]
	projects = [p for p in pages if PROJECT_TAG in p ['tags']]
	return render_template ('index.html', posts = posts, projects = projects)

@app.route ('/pages/<path:path>/')
def page (path):
	page = pages.get_or_404 (path)
	return render_template ('page.html', page = page)

@app.route ('/tags/<string:tag>/')
def tag (tag):
	tagged = [p for p in pages if tag in p ['tags']]
	return render_template ('tags.html', pages = tagged, tag = tag)

if __name__ == '__main__':
	# when building static files
	if len (sys.argv) > 1 and sys.argv [1] == 'freeze':
		freezer.freeze ()

	# when testing locally
	else:
		app.run (port = 8000)
