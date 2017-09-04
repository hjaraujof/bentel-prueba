from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='-$5u-1rrg8wkf*cmc6cgsv83=p^aqf@-arl_=q53(yb8#u3#(0')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bentel',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    },
}