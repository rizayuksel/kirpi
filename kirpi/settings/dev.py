from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEVELOPMENT = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Admin Settings
GRAPPELLI_ADMIN_TITLE = "DEVELOPMENT"
ENVIRONMENT_NAME = "DEVELOPMENT"
