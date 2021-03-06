"""
Django settings for HelloDjango project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'osucw!k0(c*^a-cgd6c9gfogzb&y6tf^eew^an0+v!&34c4w9!'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

# you can try below lines of code which was commented by commenting the previous successive lines of code
DEBUG = True
# DEBUG = False
#
# # in this i am not allowing these bad reqests ,so  it shows  you 404 error.
# ALLOWED_HOSTS = ['example.com','127.0.0.0']
#




# By default, the ALLOWED_HOSTS variable is present in settings.
# py but it's empty. The purpose of ALLOWED_HOSTS is to validate a request's (HTTP) Host header.
# Validation is done to prevent rogue users from sending fake HTTP Host headers that can potentially poison caches and password reset emails with links to malicious hosts.
# Since this issue can only present itself under an uncontrolled user environment (i.e. public/production servers),
# validation is only done when DEBUG=False.
#
# If you switch to DEBUG=False and ALLOWED_HOSTS is left empty,
#  Django will refuse to serve requests and instead report HTTP 400 bad request pages because it can't validate incoming HTTP Host headers against any allowed value.
#  Listing 1 illustrates a sample definition of ALLOWED_HOSTS.



# Application definition

# see the last list item in INSTALLED_APPS.hat is our HelloWorld app.like this evry shold be included ,if in case django make any mistake
# you have toi nclude,hopefully it wont do lik that

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HelloWorld',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Get the Project to Know About Your Application urls(We have included here Project level urls.py file ,whch consists of  evry url of the app )

ROOT_URLCONF = 'HelloDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'HelloDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

STATIC_URL = '/static/'
