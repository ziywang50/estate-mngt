# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
from os import getenv, path

from dotenv import load_dotenv

from .base import *

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

DEBUG = True

SITE_NAME = getenv("SITE_NAME")

SECRET_KEY = getenv("DJANGO_SECRET_KEY","f0W6A6IAOejN4BxQXyK_EflBZDX6S3SDOnZKQN5Xeej8AFYJQzI")

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-8@3*4dt4cs&4)$7-og-7jh&#gy^w&+%p#vy^+54%(^h*x!--p#"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv("DJANGO_ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"

EMAIL_HOST = getenv("EMAIL_HOST")

EMAIL_PORT = getenv("EMAIL_PORT")

DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")

DOMAIN = getenv("DOMAIN")