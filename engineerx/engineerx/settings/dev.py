from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%w$&w@v=&ehm)zju&6#yl)(&ymh*)%lo8r=ln_=69fxl34aets'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

INSTALLED_APPS.append('wagtail.contrib.styleguide')

try:
    from .local import *
except ImportError:
    pass
