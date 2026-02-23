"""
Production settings for main project.
"""

from .base import *
import os

# Production mode should always be False

# Allowed hosts must be set in .env
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if os.getenv("DJANGO_ALLOWED_HOSTS") else []

# Static root for collectstatic on server
STATIC_ROOT = BASE_DIR / "staticfiles"

# Celery worker settings for production

'''
┌──────────────────────────────────────────────┐
│               Celery Settings                │
└──────────────────────────────────────────────┘
'''

# Broker & Backend
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/1"

# Timezone
CELERY_TIMEZONE = "UTC"
CELERY_ENABLE_UTC = True

# Task Serialization
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Disable pickle for safety
CELERY_TASK_ACCEPT_CONTENT = ['json']

# Task execution limits
CELERY_TASK_TIME_LIMIT = 30 * 60        # Hard limit: 30 minutes
CELERY_TASK_SOFT_TIME_LIMIT = 20 * 60   # Soft limit: 20 minutes

# Default queue
CELERY_TASK_DEFAULT_QUEUE = "default"

# Worker concurrency → intentionally NOT set here!
# It will be set in dev.py and prod.py
CELERY_WORKER_CONCURRENCY = 24

# Security settings for HTTPS
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# (Optional) If using HTTPS domain:
# CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if os.getenv("CSRF_TRUSTED_ORIGINS") else []
