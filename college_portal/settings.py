import os
from pathlib import Path
import dj_database_url  # Needed for Render Database

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY CONFIGURATION ---
# Auto-detect if we are running on Render
IS_PRODUCTION = 'RENDER' in os.environ

# Keep secret key safe. Use a dummy default for local dev only.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me-for-production')

# Set DEBUG to False if on Render, True if on Local
DEBUG = not IS_PRODUCTION

ALLOWED_HOSTS = ['*'] if IS_PRODUCTION else ['127.0.0.1', 'localhost','172.29.189.111' ]

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps (Your New Structure)
    'pages',        # Home, About, Contact
    'accounts',     # Login, Register
    'clubs',        # Club logic
    'dashboard',    # Student Dashboard
    'blog',         # Blog & Articles
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <--- CRITICAL for Render Static Files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'  # Ensure your main folder is named 'core' or change this

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pointing to your global templates folder
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

WSGI_APPLICATION = 'core.wsgi.application' # Update 'core' if your config folder is named 'website'


# --- DATABASE CONFIGURATION ---
# Logic: Use SQLite locally, but switch to Supabase/Postgres automatically on Render
if IS_PRODUCTION:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # Set to your local time
USE_I18N = True
USE_TZ = True


# --- STATIC FILES (CSS, JavaScript, Images) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# This is where files go when you run 'collectstatic' (Required for Render)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Enable WhiteNoise storage for compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- MEDIA FILES (User Uploads) ---
# Currently local only. Later we will add Supabase Storage config here.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# --- LOGIN/LOGOUT REDIRECTS ---
LOGIN_REDIRECT_URL = 'dashboard'  # Where to go after login
LOGOUT_REDIRECT_URL = 'home'      # Where to go after logout
LOGIN_URL = 'login'               # Name of your login url pattern

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'