from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='@g-oc-@#wl#ht=s0r^6n*(77qxf*80vzq-gxg8&s+c@r@m0&p')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', default=True)
