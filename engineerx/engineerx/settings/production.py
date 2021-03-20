from .productionbase import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'engineerx',
        'USER': 'engineerx',
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_ENDPOINT'],
        'PORT': '5432',
    }
}