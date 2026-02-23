"""
Development settings for main project.
"""

from .base import *

# debug for dev mode
DEBUG = True

# Celery worker settings for local development
CELERY_WORKER_CONCURRENCY = 1

ALLOWED_HOSTS = []

'''
┌──────────────────────────────────────────────┐
│                MEDIA Config                  │
└──────────────────────────────────────────────┘
'''

