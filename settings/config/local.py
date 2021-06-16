from .base import *
# from .secrets import *

# GENERAL
# ------------------------------------------------------------------------------
# Configure the domain name using the environment variable
# that Azure automatically creates for us.
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = 'django-insecure-3%xzde#z7j5bx4m&m-7o050@e=$udh9xc_zz^g10-ecw9swi4w'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# INSTALLED_APPS = ['livereload'] + INSTALLED_APPS
# MIDDLEWARE = MIDDLEWARE + ['livereload.middleware.LiveReloadScript']
