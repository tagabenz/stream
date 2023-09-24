"""
Django settings for stream_app project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import base64
from pathlib import Path
from datetime import timedelta


def get_http_protocol():
    if os.getenv('ENV') == 'DEV':protocol = 'http'
    else:protocol = 'https'
    
    return protocol

def get_llhls_publisher_port():
    if os.getenv('ENV') == 'DEV':port = '3333'
    else:port=3334

    return port

def get_api_port():
    if os.getenv('ENV') == 'DEV':port = '8081'
    else:port='8082'

    return port

def get_ws_protocol():
    if os.getenv('ENV') == 'DEV':protocol='ws'
    else:protocol='wws'

    return protocol

def encode_access_token(token):
    return base64 \
        .b64encode(token.encode('utf-8')) \
        .decode('utf-8')


OME_HOST = os.getenv('OME_HOST') 
OME_VHOST_NAME = os.getenv('OME_VHOST_NAME')
OME_APP_NAME = os.getenv('OME_APP_NAME')
OME_POLICY_KEY=os.getenv('OME_POLICY_KEY')
PROTOCOL = get_http_protocol()
OME_API_PORT = get_api_port()
OME_LLHLS_PUBLISHER_PORT = get_llhls_publisher_port()
WEBSOCKET_PROTOCOL = get_ws_protocol()
if os.getenv('ENV') == 'DEV':
    OME_API_HOST = f'{PROTOCOL}://ome:{OME_API_PORT}/v1'
else:
    OME_API_HOST = f'{PROTOCOL}://{OME_HOST}:{OME_API_PORT}/v1'

OME_API_AUTH_HEADER = {'authorization': 'Basic ' + encode_access_token(os.getenv('OME_API_TOKEN'))}

# OME_STREAM_NAME = app.config['OME_STREAM_NAME']
OME_API_GET_STREAMS = OME_API_HOST + f'/vhosts/{OME_VHOST_NAME}/apps/{OME_APP_NAME}/streams'

OME_RTMP_INPUT_URL = f'rtmp://{OME_HOST}:1935/{OME_APP_NAME}'

OME_LLHLS_STREAMING_HOST = f'{PROTOCOL}://{OME_HOST}:{OME_LLHLS_PUBLISHER_PORT}'
# percent_encoded_stream_id = parse.quote(f'srt://{OME_HOST}:{ app.config["OME_SRT_PROVIDER_PORT"]}/{OME_APP_NAME}/', safe='')
# OME_SRT_INPUT_URL = f'srt://{OME_HOST}:{ app.config["OME_SRT_PROVIDER_PORT"]}?streamid={percent_encoded_stream_id}'
# OME_WEBRTC_INPUT_PROTOCOL = get_ws_protocol(
#     app.config['OME_WEBRTC_PROVIDER_ENABLE_TLS'])
# OME_WEBRTC_INPUT_HOST = f'{OME_WEBRTC_INPUT_PROTOCOL}://{OME_HOST}:{app.config["OME_WEBRTC_PROVIDER_PORT"]}'
# OME_WEBRTC_STREAMING_PROTOCOL = get_ws_protocol(
#     app.config['OME_WEBRTC_PUBLISHER_ENABLE_TLS'])
# OME_WEBRTC_STREAMING_HOST = f'{OME_WEBRTC_STREAMING_PROTOCOL}://{OME_HOST}:{app.config["OME_WEBRTC_PUBLISHER_PORT"]}'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%zz2d0a5rb0%5v)$p6l1f8n@*(8ef#tgds4-^*qx=b8p%cw_!$'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('ENV') == 'PROD':DEBUG = False
else:
    DEBUG = True
    CSRF_TRUSTED_ORIGINS=[f"https://{OME_HOST}"]
    
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'rest_framework',
    'homepage',
    'blog',
    'app_users',
    'menu',
    'studio',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'stream_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'stream_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stream_db',
        'USER': 'postgres',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   BASE_DIR / 'static'
]

MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# User
AUTH_USER_MODEL = 'app_users.Users'

LOGIN_REDIRECT_URL = '/'

SESSION_COOKIE_AGE = 30*24*60*60

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }

INTERNAL_IPS = [
    "127.0.0.1",
]


if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]