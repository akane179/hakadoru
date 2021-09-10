import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CRET_KEY = 'django-insecure-5*&beapf(lhn=u$#r%r!uie1w&nbhhj*56r30sic(d3!#p673g'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hakadorukun',
        'USER': 'akanee',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


