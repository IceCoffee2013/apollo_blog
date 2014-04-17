#!/usr/bin/env python
# coding: utf-8

import os
import sys

# os.environ['DJANGO_SETTINGS_MODULE'] = 'djblog.settings'
#
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()

sys.path.append('/var/www/apollo_blog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()