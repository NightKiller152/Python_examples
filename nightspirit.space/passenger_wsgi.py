# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1473943/data/www/nightspirit.space/portfolio')
sys.path.insert(1, '/var/www/u1473943/data/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()