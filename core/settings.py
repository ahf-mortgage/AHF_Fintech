import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xapy24exjy5!26b1d+7$v5wkh+44&(3rk^tfd=cbj#_$+dfb31'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'https://www.ahf.mortgage',
    "www.ahf.mortgage",
    'http://18.144.126.117',
     '127.0.0.1'
     ]
CSRF_TRUSTED_ORIGINS = [
  
    # 'http://www.ahf.mortgage',
    'https://www.ahf.mortgage'
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #thrid party packages
    'tailwind',
    'theme',
    'django_browser_reload',
    'crispy_forms',
    "crispy_bootstrap5",
    'widget_tweaks',
    # installed apps,
    'apps.recruiter',
    'apps.home',
    'apps.W2branchYearlyGross',
    # all auth apps
    'allauth',
    'allauth.account',
     # Configure the django-otp package.
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
    # Configure the django-otp package. Note this must be after the
    # AuthenticationMiddleware.
    'django_otp.middleware.OTPMiddleware',


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
            
                 
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                
                # `allauth` needs this from django
                'django.template.context_processors.request',
               

            ],
        },
     
       
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Replace BASE_DIR with your project's base directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'static' / 'home'
    
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Replace BASE_DIR with your project's base directory

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# tailwind config
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]




# django all auth configs

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED= True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=10 
ACCOUNT_LOGIN_ATTEMPTS_LIMIT=5
ACCOUNT_EMAIL_VERIFICATION="optional"
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=86400
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_EMAIL_CONFORMATION=180
ACCOUNT_REDIRECT_URL='/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True



# Set the allauth adapter to be the 2FA adapter.
ACCOUNT_ADAPTER = 'allauth_2fa.adapter.OTPAdapter'
ACCOUNT_FORMS = {
    'signup': 'utils.forms.AHFSignupForm'
  
  
}

# Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tinsingjobs2k@gmail.com'
EMAIL_HOST_PASSWORD = 'vavkndyvafegycua'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



# django auth config
LOGIN_REDIRECT_URL = "/"


# crispy form config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"




# Configure your default site. See
SITE_ID = 1
VERSION = 0.002
