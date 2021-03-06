import dj_database_url

from myportfolio.settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"
