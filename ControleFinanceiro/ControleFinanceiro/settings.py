# -*- coding: utf-8 -*-

"""
Django settings for ControleFinanceiro project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import sys
# Set default encoding to 'UTF-8' instead of 'ascii'
# http://stackoverflow.com/questions/11741574/how-to-set-the-default-encoding-to-utf-8-in-python
# Bad things might happen though
reload(sys)
sys.setdefaultencoding("UTF8")



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vl&wwbv+@u6&ehv*+ismc*^6gth3e)!4q#%p^t-ynf9zdt#a-0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'sistema'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ControleFinanceiro.urls'

WSGI_APPLICATION = 'ControleFinanceiro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

#postgreeSQl

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',                      
        'USER': 'postgres',                   
        'PASSWORD': '1234',              
        'HOST': 'localhost',                      
        'PORT': '5432',           
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#login settings
LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"


#email settings
DEFAULT_FROM_EMAIL = "fczanardo@hotmail.com"
EMAIL_HOST='smtp.live.com'
EMAIL_PORT=587
EMAIL_HOST_USER="fczanardo"
EMAIL_HOST_PASSWORD="fa89ju67"
EMAIL_USE_TLS=True

STATIC_URL = '/static/'