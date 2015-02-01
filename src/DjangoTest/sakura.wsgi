# -*- coding: utf-8 -*-

import os,sys

sys.path.append('/home/fukajun/django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ProjectAdminTool.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
