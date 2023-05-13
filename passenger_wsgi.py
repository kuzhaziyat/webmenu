# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, '/var/www/u1680963/data/www/thedouble.ru/delivery')

sys.path.insert(1, '/var/www/u1680963/data/venv/lib/python3.9/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'delivery.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()