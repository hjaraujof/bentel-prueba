from .base import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = env('DJANGO_SECRET_KEY', default='a$xybrfuqll#4hxrl&w#z(!r4_$0&@i_9vzf%l+k0)uzvmc1nue')
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bentel',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'db',
        'PORT': '5432'
    },
}
STATIC_ROOT = '/static'