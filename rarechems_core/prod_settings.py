import dj_database_url

from rarechems_core.settings import *

SECRET_KEY = os.environ['SECRET_KEY']



DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_AGE=86400
CART_SESSION_ID='cart'

DATABASES['default'] = dj_database_url.config(conn_max_age=500)

#'EMAIL_USE_TLS = True
#EMAIL_HOST = 'mail.infomaniak.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'contact@tradingview.com'
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend

CLOUDINARY_URL = os.environ['CLOUDINARY_URL']

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

ADMINS = [
    ('Tview', 'contact@trailingview.com',)
]