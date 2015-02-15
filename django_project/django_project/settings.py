"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import ConfigParser

DIGITAL_OCEAN_PRODUCTION = False
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if "DIGITAL_OCEAN" in os.environ:
    DIGITAL_OCEAN_PRODUCTION = True
    try:
        production_settings = ConfigParser.ConfigParser()
        production_settings.readfp(open(os.path.join(BASE_DIR, "django_project/settings.cfg")))
    except IOError:
        DIGITAL_OCEAN_PRODUCTION = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if DIGITAL_OCEAN_PRODUCTION:
    SECRET_KEY = production_settings.get("KEYS", "SECRET_KEY")
else:
    SECRET_KEY = "_e76b0pz(6v-=w+ga44q585k*6_6i#y88s$sgu8!)u7x459f97"

# SECURITY WARNING: don't run with debug turned on in production!
if DIGITAL_OCEAN_PRODUCTION:
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["104.131.170.176"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "home"
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if DIGITAL_OCEAN_PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': production_settings.get("database", "name"),
            'USER': production_settings.get("database", "user"),
            'PASSWORD': production_settings.get("database", "password"),
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'django_project/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

STATIC_URL = '/static/'
