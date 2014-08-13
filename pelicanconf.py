#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Levi Thomason'
SITENAME = u"Levi Thomason's Blog"
SITEURL = 'http://www.levithomason.com/blog'

# Prettify text
TYPOGRIFY = True

THEME = './../pelican-themes/BT3-Flat'

# flow THEME = './../pelican-themes/SoMA'
#  flow THEME = './../pelican-themes/SoMA2'
# angle tape text THEME = './../pelican-themes/bold'
# font THEME = './../pelican-themes/chunk'
# not bad idea THEME = './../pelican-themes/html5-dopetrope'
# close THEME = './../pelican-themes/notebook'
# fav THEME = './../pelican-themes/pelican-cait'
# close THEME = './../pelican-themes/pure'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # Apple Touch Icons
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'extra/apple-touch-icon-60x60.png': {'path': 'apple-touch-icon-60x60.png'},
    'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
}

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Levi\'s Home', 'http://www.levithomason.com'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/levithomason'),
    ('Google+', 'https://plus.google.com/u/0/+LeviThomason7'),
    ('Twitter', 'https://twitter.com/levithomason7'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
