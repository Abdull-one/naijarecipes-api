import os
from pathlib import Path
from datetime import timedelta

# ------------------------
# Paths
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# Security
# ------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-in-prod')
DEBUG = True  # Turn to False in production
ALLOWED_HOSTS = []

# ------------------------
# Installed Apps
# ------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Local apps
    'users',
]

# ------------------------
# Middleware
# ------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS support
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------
# URLs & WSGI
# ------------------------
ROOT_URLCONF = 'naijarecipes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'naijarecipes.wsgi.application'

# ------------------------
# Database
# ------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL in production
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------
# Authentication
# ------------------------
AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# ------------------------
# Password validation
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------
# Internationalization
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# ------------------------
# Static & Media files
# ------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------
# CORS settings (Allow frontend to connect)
# ------------------------
CORS_ALLOW_ALL_ORIGINS = True  # For development only
# In production, set: CORS_ALLOWED_ORIGINS = ['https://yourfrontend.com']

# ------------------------
# Default primary key field type
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
