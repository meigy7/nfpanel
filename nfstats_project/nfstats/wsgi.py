"""
WSGI config for nfstats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


# path = '/var/www/nfstats_project/nfstatss'
# if path not in sys.path:
#     sys.path.append(path)
chdir='/var/www/nfstats_projectt/'


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nfstats.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nfstats.settings')


application = get_wsgi_application()
