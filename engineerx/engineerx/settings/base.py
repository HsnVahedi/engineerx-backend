"""
Django settings for engineerx project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'authentication',
    'home',
    'search',
    'posts',
    'images',
    'common',
    'api',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.api.v2',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'engineerx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'engineerx.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DOWNLOADS_ROOT = os.path.join(MEDIA_ROOT, 'downloads')
IMAGE_DOWNLOADS_DIR = os.path.join(DOWNLOADS_ROOT, 'images')
AVATAR_DOWNLOADS_DIR = os.path.join(DOWNLOADS_ROOT, 'avatars')

# Wagtail settings

WAGTAIL_SITE_NAME = "engineerx"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

AUTH_USER_MODEL = "authentication.User"

# WAGTAIL_USER_EDIT_FORM = 'authentication.forms.UserEditForm'
# WAGTAIL_USER_CREATION_FORM = 'authentication.forms.UserCreationForm'
# WAGTAIL_USER_CUSTOM_FIELDS = ['country', 'status']

WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True

# DJANGO_SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
# DJANGO_SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@admin.com')
# DJANGO_SUPERUSER_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin password')
# DJANGO_SUPERUSER_FIRSTNAME = os.environ.get('DJANGO_SUPERUSER_FIRSTNAME', 'admin')
# DJANGO_SUPERUSER_LASTNAME = os.environ.get('DJANGO_SUPERUSER_LASTNAME', 'admin')

INITDB_USERS_SIZE = int(os.environ.get('INITDB_USERS_SIZE', 50))
INITDB_EDITORS_SIZE = int(os.environ.get('INITDB_EDITORS_SIZE', 50))
INITDB_MODERATORS_SIZE = int(os.environ.get('INITDB_MODERATORS_SIZE', 50))
INITDB_POSTS_SIZE = int(os.environ.get('INITDB_POSTS_SIZE', 50))

DEFAULT_RICHTEXT_FEATURES = [
    'h3', 'h4', 'h5', 'h6',
    'bold', 'italic',
    'ol', 'ul',
    'hr', 'link', 'document-link'
]

RANDOM_IMAGE_URL = 'https://picsum.photos'
RANDOM_AVATAR_URL = 'https://i.pravatar.cc'

FRONTEND_URL = os.environ.get('FRONTEND_URL', '')