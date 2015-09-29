
"""
Django settings for hiretech project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'haystack',
    'markdown_deux',
    'nocaptcha_recaptcha',
    'users',
    'jobs',
    'companies',
    'accounts',
    'posts',
    'compressor',
    'taggit',
    'imagekit',
    'drip',
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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'hiretech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'hiretech.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Haystack ElasticSearch
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'HireTech Noreply <noreply@hiretech.io>'
DEFAULT_DOMAIN = 'hiretech.io'
SERVER_EMAIL = 'jobs@hiretech.io'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'alex@hiretech.io'
EMAIL_HOST_PASSWORD = os.environ['MANDRILL_API_KEY']


DRIP_MESSAGE_CLASSES = {
    'hiretechdefault': 'hiretech.email.DefaultDripEmail',
}

LOGIN_URL = '/login/'

MEDIA_ROOT = normpath(join('media'))
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = normpath(join('static'))
STATIC_URL = '/static/'
#STATICFILES_DIRS = (
#    normpath(join(SITE_ROOT, 'static')),
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Google Recaptcha
NORECAPTCHA_SITE_KEY = '6Lc6AgwTAAAAACed2E7SeDaz6AeVmuKFzL8_5h0o'
NORECAPTCHA_SECRET_KEY = '6Lc6AgwTAAAAAK6A-TE2ApoK4oxCaKeqiEcDDXg9'

# Sass compiler
COMPRESS_ENABLED = True
COMPRESS_ROOT = normpath(join('static'))
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Markdown
MARKDOWN_DEUX_STYLES = {
    "default": {
        "safe_mode": "escape",
    },
}

# Django Suit Config
SUIT_CONFIG = {
    'ADMIN_NAME': 'HireTech',
    'MENU': (
        {'app': 'accounts', 'label': 'Accounts', 'icon':'icon-leaf'},
        {'app': 'jobs', 'label': 'Jobs', 'icon':'icon-tasks'},
        {'app': 'taggit', 'label': 'Tags', 'icon':'icon-tag'},
        {'app': 'companies', 'label': 'Companies', 'icon':'icon-briefcase'},
        {'app': 'auth', 'label': 'Auth', 'icon':'icon-lock'},
        {'app': 'users', 'label': 'User Profiles', 'icon':'icon-user'},
        {'app': 'drip', 'label': 'Drips', 'icon':'icon-envelope'},
        {'app': 'posts', 'label': 'Posts', 'icon':'icon-pencil'},
    )
}
