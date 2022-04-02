import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-akr@-%n+6fpd-iqfuw$vdd&n#-)5529#20+*f4i#ui89w$7iqv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'newapp',
    'django_filters',
    'sign',
    'protect',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'django_apscheduler',

]

DEFAULT_FROM_EMAIL = 'testpost111111@yandex.by'


SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # путь, где лежат нами созданные шаблоны по умолчанию
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "newapp/static"
]


LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'testpost111111'
EMAIL_HOST_PASSWORD = 'qwsazx12'
EMAIL_USE_SSL = True

# список всех админов в формате ('имя', 'их почта')
# если хотим отправлять письма только админам (статут пользователя = все права)
ADMINS = [
    ('Niger', 'testpost222222@yandex.by'),
    ('Induk', 'induk-manduk@mail.ru')
]

MANAGERS =[
    ('Niger', 'testpost222222@yandex.by'),
    ('Induk', 'induk-manduk@mail.ru')
]

SERVER_EMAIL = 'testpost111111@yandex.by'  # это будет у нас вместо аргумента FROM в массовой рассылке

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTIFICTION_METHOD = 'email'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://:K2qfVC40dQIPdMO3gzlEdIfFTVS4gncV@redis-19994.c1.asia-northeast1-1.gce.cloud.redislabs.com:19994/0'
CELERY_RESULT_BACKEND = 'redis://:K2qfVC40dQIPdMO3gzlEdIfFTVS4gncV@redis-19994.c1.asia-northeast1-1.gce.cloud.redislabs.com:19994/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug_console': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s',
        },
        'warning_console': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
        'error_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general_security_log': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'mail_log': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        }
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_console'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_console'
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_security_log'
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_security_log'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },
        'mail_admin': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail_log'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'file_general'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        }
    }
}