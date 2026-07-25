from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")

DEBUG = True

ALLOWED_HOSTS = [
    "velvetcreature.onrender.com",
    "www.velvetcreature.fr",
    "velvetcreature.fr",
    "localhost",
    "127.0.0.1",
]


# =========================================================
# APPS
# =========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
    'products',
    'categories',
    'cart',
    'orders',
    'custom_orders',
    'accounts',
    "wishlist",
    "reviews",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
]


ROOT_URLCONF = 'config.urls'


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / "templates"
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.debug',

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',

                'cart.context_processors.cart_context',

            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# =========================================================
# DATABASE
# =========================================================

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'sqlite:///' + str(BASE_DIR / 'db.sqlite3'))
    )
}


# =========================================================
# INTERNATIONALIZATION
# =========================================================

USE_I18N = True


LANGUAGE_CODE = "fr"

LANGUAGES = [

    ("en", "English"),

    ("fr", "Français"),

    ("sk", "Slovensky"),

]

LOCALE_PATHS = [

    BASE_DIR / "locale",

]

LANGUAGE_COOKIE_NAME = "django_language"

LANGUAGE_COOKIE_AGE = 1209600


# =========================================================
# STATIC FILES
# =========================================================

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [

    BASE_DIR / "static",

]


# =========================================================
# MEDIA FILES (PRODUCT IMAGES)
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# STRIPE
# =========================================================

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")


# =========================================================
# EMAIL
# =========================================================



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True


EMAIL_HOST_USER = "szlovakl333@gmail.com"

EMAIL_HOST_PASSWORD = "iqwcpohfvyhjeqvx"


DEFAULT_FROM_EMAIL = (
    "Velvet Creature <szlovakl333@gmail.com>"
)


DEFAULT_ADMIN_EMAIL = (
    "TVÔJ_GMAIL@gmail.com"
)
# =========================================================
# DEFAULT
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"