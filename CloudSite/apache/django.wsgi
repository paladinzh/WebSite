import os
import sys
path = '/home/paladin/Space/hgfs/depot/WebSite/CloudSite'
if path not in sys.path:
    sys.path.insert(0, '/home/paladin/Space/hgfs/depot/WebSite/CloudSite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'CloudSite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

