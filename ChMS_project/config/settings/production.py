# settings/production.py
from .base import *

DEBUG = False
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GNT_ChMS_MyDB',
        'USER': 'pekUrsTruly',
        'PASSWORD': 'GloriaTai4ndP#k',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

#INSTALLED_APPS += ("debug_toolbar", )
