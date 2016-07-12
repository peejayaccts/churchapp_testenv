# settings/local_pj.py
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'USER': '',
        #'PASSWORD': '',
        #'HOST': 'localhost',
        #'PORT': '',
    }
}

#INSTALLED_APPS += ("debug_toolbar", )
