# Django settings for demoproject project.
import sys, os


here = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(here, '..', '..')))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'DEMODB.sqlite', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Bangkok'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(here, 'media')
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
SECRET_KEY = 'c73*n!y=)tziu^2)y*@5i2^)$8z$tx#b9*_r3i6o1ohxo%*2^a'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',)

ROOT_URLCONF = 'demoproject.urls'
WSGI_APPLICATION = 'demoproject.wsgi.application'

AUTHENTICATION_BACKENDS = ('demoproject.backends.AnyUserBackend',)

INSTALLED_APPS = (
    'ichangelist',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'demoproject.demoapp')

