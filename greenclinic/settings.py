from pathlib import Path
import dj_database_url
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zvu+dg$#p*2!^ev^xpx#esohj9u@&ux%%rl*5m%m+pp*8vahh5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clinic',
    'rest_framework',
    'cloudinary',
    'corsheaders',
    'storages',  # For DigitalOcean Spaces
    'drf_spectacular',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Ensure CORS Middleware is separate
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Correct CSRF Middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DRF Configuration
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

ROOT_URLCONF = 'greenclinic.urls'

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

WSGI_APPLICATION = 'greenclinic.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:yXAYdpBoTwaTBVolGdwRoWzZXLDAHbcl@monorail.proxy.rlwy.net:31743/railway'
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Manually load environment variables
env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):  # Ignore empty lines and comments
                key, value = line.strip().split("=", 1)  # Split by first '=' only
                os.environ[key] = value  # Set environment variable


# DigitalOcean Spaces Configuration
AWS_ACCESS_KEY_ID = "DO801LBXMMR3YQH7QTK8"
AWS_SECRET_ACCESS_KEY = "mVZtTlHATh2Ju5nfGqSpAV5x2J8QHXWLfCKX5DXUV8A"
AWS_STORAGE_BUCKET_NAME = "clicksorderingsystem"
AWS_S3_ENDPOINT_URL = f"https://nyc3.digitaloceanspaces.com"
AWS_REGION = "nyc3"

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL.replace('https://', '')}"



AWS_DEFAULT_ACL = None  # Prevents objects from being private
AWS_QUERYSTRING_AUTH = False  # Removes authentication tokens from URLs
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache files for faster load times
    'ACL': 'public-read',  # This ensures uploaded files are publicly accessible
}

# Add WebP to the allowed content types
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Add this line
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

# CLOUDINARY = {
#     'cloud_name': 'doda8ylux',
#     'api_key': '686594864282927',
#     'api_secret': 'Mn4ytMqtWPv0Srw0DbEl3-1FQ4A',
# }

