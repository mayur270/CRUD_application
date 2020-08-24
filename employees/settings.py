import os
from pathlib import Path
import dotenv

dotenv.load_dotenv()

####################### BASE_DIR ######################

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

#######################################################

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['rocky-caverns-53277.herokuapp.com', 'localhost', '127.0.0.1']

########################## Apps ########################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd Party apps
    'allauth',
    'allauth.account',
    'widget_tweaks',
    'phone_field',

    # Local Apps
    'contacts.apps.ContactsConfig',
    'users.apps.UsersConfig',
]

##################### AUTH_BACKEND ######################

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend',
)

####################### Middleware #######################

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

######################### Cache #######################

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''

######################## URLCONF ######################

ROOT_URLCONF = 'employees.urls'

####################### Template ######################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

######################### WSGI #######################

WSGI_APPLICATION = 'employees.wsgi.application'

####################### Database #####################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

################# Password validation ################

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

################## Internationalization ###############

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#################### Static files ####################

STATIC_URL = '/static/'
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder",]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#################### Django AllAuth ###################

SITE_ID = 1

LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'login'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_ADAPTER = 'users.adapter.AccountAdapter' # Removes SignUp Form

################# Custom User Model ##################

AUTH_USER_MODEL = 'users.CustomUser'

#################### PRODUCTION #####################
# 
# if ENVIRONMENT == 'production':
#     SECURE_BROWSER_XSS_FILTER = True                                # XSS Attacks Protection
#     X_FRAME_OPTIONS = 'DENY'                                        # Clickjacking Protection
#     SECURE_SSL_REDIRECT = True                                      # Non-HTTPS to be reidrected to HTTPS
#     SECURE_HSTS_SECONDS = 3600                                      # HTTP Strict Transport Security (HSTS)
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True                           # HTTP Strict Transport Security (HSTS)
#     SECURE_HSTS_PRELOAD = True                                      # HTTP Strict Transport Security (HSTS)
#     SECURE_CONTENT_TYPE_NOSNIFF = True                              # NoSniff Protection
#     SESSION_COOKIE_SECURE = True                                    # Cookie Protection
#     CSRF_COOKIE_SECURE = True                                       # Cookie Protection
#     DEBUG = False                                                   # Debug Protection
#     SECURE_REFERRER_POLICY = "same-origin"                          # Referrer-Policy Protection
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')   # Proxy-SSL-Header Protection
