from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = pro_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['flexroadshield.com', 'www.flexroadshield.com']


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME, # set this variable in secrects.py
        'USER': DATABASE_USER, # set this variable in secrects.py
        'PASSWORD': DATABASE_PASS, # set this variable in secrects.py
        'HOST': 'localhost',
        'PORT': '',
    }
}