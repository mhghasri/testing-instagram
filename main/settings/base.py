"""
Base settings for main project.
"""

from dotenv import load_dotenv
from pathlib import Path
import logging
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# /project_root/main/settings/base.py  →  parent → settings  → parent → main → parent → project_root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
logger = logging.getLogger(__name__)

'''
┌──────────────────────────────────────────────┐
│                  ENV Config                  │
└──────────────────────────────────────────────┘
'''

load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS: list[str] = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # 'daphne',                           # ASGI config
    "django.contrib.staticfiles",
    "rest_framework",                   # drf
    # 'rest_framework.authtoken',       # rest authentication
    'rest_framework_simplejwt',         # jwt authentication
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

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",  
                # "customer.context_processors.interaction_assignment_processors",      # -> messsage context_processors
                # "customer.context_processors.interaction_reminder_processors",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

'''
┌──────────────────────────────────────────────┐
│                Database Config               │
└──────────────────────────────────────────────┘
'''

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Password validation

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


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True

'''
┌──────────────────────────────────────────────┐
│              MEDIA / STATIC Config           │
└──────────────────────────────────────────────┘
'''

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "assets"
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user model
# AUTH_USER_MODEL = "account.User"

'''
┌──────────────────────────────────────────────┐
│                 REST_FRAMEWORK               │
└──────────────────────────────────────────────┘
'''

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',                  # drf authentication
        # 'rest_framework.authentication.BasicAuthentication',                  # drf authentication
        # 'rest_framework.authentication.SessionAuthentication',                # drf session
        'rest_framework_simplejwt.authentication.JWTAuthentication',            # jwt authentication
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',               # swagger

}

'''
╭──────────────────────────────────────────────╮
│                Redis Config                  │
╰──────────────────────────────────────────────╯
''' 

REDIS_HOST = os.getenv("REDIS_HOST", "redis")  # پیش‌فرض: اسم سرویس ردیس در docker-compose
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB_CACHE = os.getenv("REDIS_DB_CACHE", "1")

# بدون پسورد
REDIS_CACHE_LOCATION = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_CACHE}"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


'''
╭──────────────────────────────────────────────╮
│          django Channel Redis Config         │
╰──────────────────────────────────────────────╯
'''

REDIS_DB_CHANNELS = os.getenv("REDIS_DB_CHANNELS", "2") 
REDIS_HOST_WITH_AUTH = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_CHANNELS}"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_HOST_WITH_AUTH],
        },
    },
}

ASGI_APPLICATION = "main.asgi.application"

'''
┌──────────────────────────────────────────────┐
│                Celery Settings               │
└──────────────────────────────────────────────┘
'''

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/1"

CELERY_TIMEZONE = "UTC"
CELERY_ENABLE_UTC = True

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_ACCEPT_CONTENT = ["json"]

CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 20 * 60
CELERY_TASK_DEFAULT_QUEUE = "default"

'''
╭──────────────────────────────────────────────╮
│                   JWT Config                 │
╰──────────────────────────────────────────────╯
'''
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}