from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask (__name__)
app.config.from_object (__name__)
pages = FlatPages (app)

'''
Site Structure:

home/about me
|	|
|	--personal info, links to other parts of the site, i.e. recent blog posts, projects, etc.
|
--portfolio
|	|
|	--various projects
|
--blog
|	|
|	--various posts
|
--resume
|	|
|	--link to resume as pdf
|
--contact
|	|
|	--contact info
|
--search
	|
	--search text, tags
'''

@app.route ('/')
def index ():
	return render_template ('index.html', pages = pages)

@app.route ('/<path:path>/')
def page (path):
	page = pages.get_or_404 (path)
	return render_template ('page.html', page = page)

@app.route ('/tags/<string:tag>/')
def tag (tag):
	tagged = [p for p in pages if tag in p.meta.get ('tags', [])]
	return render_template ('tags.html', pages = tagged, tag = tag)

if __name__ == '__main__':
	app.run (port = 8000)