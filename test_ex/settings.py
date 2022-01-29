from pathlib import Path

import django_heroku
import dj_database_url

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = "django-insecure-y0)11y**8j8&fq4g*sn&l(*fa%_$p@$lvf37%(fdfq=@q39igy"

DEBUG = True

ALLOWED_HOSTS = ['*.herokuapp.com','127.0.0.1:8000','.herokuapp.com', 'localhost', '127.0.0.1']


INSTALLED_APPS = [
    # admin
    "jet",
    "psycopg2",
    'django_heroku',
    # standart
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # packages
    "rest_auth",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
    "django_celery_results",
    "django_celery_beat",
    # apps
    "posts",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "test_ex.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "test_ex.wsgi.application"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'develops_today_db',
#         'USER': 'develops_today_user',
#         'PASSWORD': 'develops_today_password',
#         'HOST': 'postgresdb',
#         'PORT': '5432',
#     }
# }

DATABASES = dict()
db_from_env = dj_database_url.config(conn_max_age=600,default='postgres://kvczvdlxoqbwfx:0dee2680b2597255642c8b62bc5751ef3fb4e8be0e858f9df88bfaa653386797@ec2-3-210-12-0.compute-1.amazonaws.com:5432/dffccau899jhoj')
DATABASES['default'] = db_from_env


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


SWAGGER_SETTINGS = {
    "PERSIT_AUTH": True,
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
}

# jet settings

JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]


CELERY_BROKER_URL = "redis://redis:6379"
CELERY_BROKER_TRANSPORT = "redis"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Bishkek"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_IMPORTS = ("posts.tasks",)
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_ACKS_LATE = True
CELERY_ACKS_ON_FAILURE_OR_TIMEOUT = True

# # celery beat

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
