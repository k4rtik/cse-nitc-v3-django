import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'csed.settings'

sys.path.append('/home/django')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

