"""
Django settings for amzfunnel project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dotenv
from datetime import timedelta
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-f&3o3hf)m)kf0hp-zs2zvab7-u4tx_rmu*s$y)g*-!5u+t)9q9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*','127.0.0.1',".herokuapp.com",'localhost','192.168.1.147', 'vigilant-curiosity-production.up.railway.app', 'api.top8.uk']

# comementar para development
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
# ////////
SECURE_SSL_REDIRECT = True  ## comment for development
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  ## comment for development
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True  # Set to True in production

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# comment for development

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
## comentar para development

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## apps instaladas
    'core',
    'rest_framework',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'rest_framework_simplejwt.token_blacklist',
    'users',

]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Celery settings
# CELERY_BROKER_URL = 'redis://:GDs3q4HqYtQTrEWl9iCtpyibSH8bJqVKqYlFyHtkibk1WFROvHbk5wenI9AeSs8N@192.168.1.194:6379/0' # local
CELERY_BROKER_URL = 'redis://default:ReXKWYdCtYMSkUrNXAEohQUguUATFmsz@junction.proxy.rlwy.net:14836' # RAILWAY
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'redis://:GDs3q4HqYtQTrEWl9iCtpyibSH8bJqVKqYlFyHtkibk1WFROvHbk5wenI9AeSs8N@192.168.1.194:6379/0' # local
CELERY_RESULT_BACKEND = 'redis://default:ReXKWYdCtYMSkUrNXAEohQUguUATFmsz@junction.proxy.rlwy.net:14836' # RAILWAY
# CELERY_BEAT_SCHEDULE = {
#     'scrape-every-5-minutes': {
#         'task': 'your_app.tasks.scrape_urls_from_db_task',
#         'schedule': 300.0,  # Scrapes every 5 minutes
#     },
# }
CELERY_WORKER_CONCURRENCY = 4  # Adjust based on your needs
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
CELERY_TASK_RESULT_EXPIRES = 60  # Time in seconds (e.g., 1 hour)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=240),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',

    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=240),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=31),
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


ROOT_URLCONF = 'amzfunnel.urls'

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

WSGI_APPLICATION = 'amzfunnel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['NAME_DB'],
#         'USER': os.environ['USER_DB'],
#         'PASSWORD': os.environ['PASSWORD_DB'],
#         'HOST': os.environ['HOST_DB'],
#         'PORT': os.environ['PORT_DB'],
#     }
# }


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# DATABASES = {
#     'default': dj_database_url.config(
#         default='postgresql://postgres:DC1EDA4da34D2b36aC24fEE263c2gge5@192.168.1.188:5432/railway'
#     )
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
