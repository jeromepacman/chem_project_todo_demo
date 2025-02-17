import os

from pathlib import Path

from secret_key_generator import secret_key_generator

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR=Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


SECRET_KEY=secret_key_generator.generate()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=True

ALLOWED_HOSTS=[]

EMAIL_HOST='localhost'
EMAIL_PORT=1025

LOGIN_URL='login'
LOGIN_REDIRECT_URL='frontpage'
LOGOUT_REDIRECT_URL='frontpage'

# Cart

SESSION_COOKIE_AGE=1800
CART_SESSION_ID='cart'

# Application definition

INSTALLED_APPS=[
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'cloudinary_storage',
    'cloudinary',

    'apps.cart',
    'apps.coupon',
    'apps.core',
    'apps.newsletter',
    'apps.order',
    'apps.store',
    'apps.userprofile'
]

MIDDLEWARE=[
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF='rarechems_core.urls'

TEMPLATES=[
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
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION='rarechems_core.wsgi.application'

SITE_ID=1
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS=[
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE='en-en'

TIME_ZONE='Europe/Paris'

USE_I18N=True

USE_L10N=True

USE_TZ=True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL='/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

# API test keys

STRIPE_API_KEY_PUBLISHABLE="pk_test_51HIHiuKBJV2qfWbD2gQe6aqanfw6Eyul5P02KeOuSR1UMuaV4TxEtaQyzr9DbLITSZweL7XjK3p74swcGYrE2qEX00Hz7GmhMI"
STRIPE_API_KEY_HIDDEN="sk_test_51HIHiuKBJV2qfWbD4I9pAODack7r7r9LJOY65zSFx7jUUwgy2nfKEgQGvorv1p2xP7tgMsJ5N9EW7K1lBdPnFnyK00kdrS27cj"

RAZORPAY_API_KEY_PUBLISHABLE="rzp_test_Wj7ujrjP6ULkuq"
RAZORPAY_API_KEY_HIDDEN="WT8djoNtYSAzA28BrhryFL0f"

PAYPAL_API_KEY_PUBLISHABLE="Ab5gaq5YlFHQTAgbcIW79GV4wE7ObsefiPyNMNV87z1-2JzdNhHpOfGKIduOM1qItLgLI3eA2Z3PIHLw"
PAYPAL_API_KEY_HIDDEN="aEKFH985N2oOIFWOeS7rdq2Nht6CdztTVDDjDuQCMIBKcAbjyL-Z3ZY9DeznZSaFbQTp1H4o7CrxgwjX4x"
