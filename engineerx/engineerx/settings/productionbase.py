from .base import *
import os

DEBUG = False

SECRET_KEY = '%w$&w@v=&ehm)zju&6#yl)(&ymh*)%lo8r=ln_=69fxl34aets'
ALLOWED_HOSTS = ['*']

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

try:
    from .local import *
except ImportError:
    pass
