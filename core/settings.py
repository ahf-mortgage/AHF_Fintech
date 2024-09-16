import os
from datetime import timedelta
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #config('DEBUG', default=False, cast=bool) #True

ALLOWED_HOSTS = [
    'https://www.ahf.mortgage',
    "www.ahf.mortgage",
    'http://18.144.126.117',
     '127.0.0.1',
     'localhost'
     ]
# CSRF_TRUSTED_ORIGINS = [
#     'http://www.ahf.mortgage',
#     'https://www.ahf.mortgage'
#     ]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# Application definition
INSTALLED_APPS = [

    'django_nvd3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #thrid party packages
    'theme',
    'django_browser_reload',
    'crispy_forms',
    "crispy_bootstrap5",
    'widget_tweaks',
    'rest_framework',
    'djoser',
    'corsheaders',
    'compressor', 
    # installed apps,
    'apps.recruiter',
    'apps.home',
    'apps.W2branchYearlyGross',
    'apps.RevenueShare',
    'apps.accounts',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 
            BASE_DIR / 'templates',
            BASE_DIR / 'templates' / 'screens',
            BASE_DIR / 'templates' / 'components',
            BASE_DIR / 'templates' / 'includes',
            "/home/tinsae/Desktop/AHF_Fintech/frontend/ahf/"
            
                 
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages', 
                'apps.home.context_processors.global_variables',
                # `allauth` needs this from django
                'django.template.context_processors.request',

            ],
        },
     
       
    },
]

COMPRESS_ROOT = BASE_DIR / 'static'
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)


WSGI_APPLICATION = 'core.wsgi.application'
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',)
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db4.sqlite4',
    }
}



# django all auth configs
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
]

DJANGO_SECURE_OBJECT_REGISTRY = {
    'TOKEN_LIFESPAN': timedelta(hours=2),  # Set the default lifespan to 2 hours
}

PASSWORD_RESET_CONFIRM_URL = "https://www.ahf.morgage/auth/"

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Replace BASE_DIR with your project's base directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'static' / 'home'
    
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Replace BASE_DIR with your project's base directory

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# tailwind config
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]




EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)


# Email server configuration
EMAIL_HOST          = config('EMAIL_HOST', default='smtp.gmail.com') 
EMAIL_HOST_USER     = config('EMAIL_HOST_USER', default=25)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default=25) 
EMAIL_PORT          = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS       = config('EMAIL_USE_TLS', default=25) #True

PASSWORD_RESET_CONFIRM_UR = "http://12.0.0.1:8000"


# django auth config

LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/'

# crispy form config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"



#Hello 
# Configure your default site. See
SITE_ID = 1
VERSION = 0.005


