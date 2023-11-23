"""
WSGI config for recipes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/recipes') # adjust as

load_dotenv(os.path.join(project_folder, '.env'))
# assuming your django settings file is at '/home/username/mysite/mysite/settings.py'
#  and your manage.py is is at '/home/username/mysite/manage.py'
path = '/home/Irafita/recipes'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'recipes.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()