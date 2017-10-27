#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vipin G S'
SITENAME = 'VipinGS Blog'
SITEURL = 'https://vipings.github.io/'
BIO = 'Roller-coaster journey with data science'
PATH = 'content'
PROFILE_IMAGE = 'profile.jpg'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'gs.vipin@yahoo.in'),
          ('linkedin', 'https://www.linkedin.com/in/gsvipin/'),
	  ('github','https://github.com/vipings/' ),
	  ('twitter', 'https://twitter.com/vipingsnair/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
THEME = 'pelican-hyde'
