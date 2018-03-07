import os
from unipath import Path

PROJECT_DIR = Path(__file__).parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This system is no longer deployed any where and it won't be in the future, thus our repo was made publicly accesibile. 
SECRET_KEY = '<INSERT YOUR OWN SECRET KEY HERE>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['67.207.72.58', 'www.sioforeninger.no', 'sioforeninger.no']

# TEST_RUNNER = 'django_behave.runner.DjangoBehaveTestSuiteRunner'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition
# Creation of an app must be added here & packages
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    # Packages
    'bootstrap3',
    'coverage',
    'datetimewidget',
    'behave_django',
    'session_security',
    # 'django_popup_view_field',
    'crispy_forms',
    'anymail',


    # Apps
    'SiO.member',
    'SiO.CoAdmin',
    'SiO.chart',
    'SiO.core',
    'SiO.calapp',
    'SiO.post',
]


# This will add the name of User model
AUTH_USER_MODEL = 'CoAdmin.Administrator'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
]

ROOT_URLCONF = 'SiO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates')
        ],
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

WSGI_APPLICATION = 'SiO.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_test_local',
        'USER': 'postgres',
        'PASSWORD': 'illievski',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

# Paths for LOGIN
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_URL = '/'
LOGIN_URL = '/login'

# Session-timer
SESSION_SECURITY_EXPIRE_AFTER = 3600
SESSION_SECURITY_WARN_AFTER = 3000
# SESSION_SECURITY_EXPIRE_AFTER = 10
# SESSION_SECURITY_WARN_AFTER = 5
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

ANYMAIL = {
    #Add your own mailsettings here
    "MAILGUN_API_KEY": "",
    "MAILGUN_SENDER_DOMAIN": '',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "TestSite Team <noreply@sioforeninger.no>"  # if you don't already have this in settings
