#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Toulibre'
SITENAME = u'Capitole du Libre - le blog'
SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = u'L\'événement autour de Logiciel Libre à Toulouse'
THEME = 'cdltheme-blog'
CSS_FILE = 'styles.css'

OUTPUT_PATH = 'output/'

PLUGIN_PATHS = ["./pelican-plugins-master"]
PLUGINS = ['html_rst_directive']

PATH = 'src'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['liens']


ARTICLE_URL = '{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'

# static paths will be copied under the same name
STATIC_PATHS = ["photos",]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  (
    ('Toulibre', 'http://www.toulibre.org/'),
    ('Ubuntu-fr', 'http://www.ubuntu-fr.org/'),
         )

# Social widget
SOCIAL = (
          ('Identica', 'identica', 'http://identi.ca/toulibreorg'),
          ('Twitter', 'twitter', 'https://twitter.com/toulibreorg'),
          ('Google+', 'google', 'https://plus.google.com/b/109128243242581226442/109128243242581226442/posts'),
          ('Lanyrd', 'lanyrd', 'http://lanyrd.com/2013/capitole-du-libre/'),
         )

TWITTER_USERNAME = 'Toulibreorg'
DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
