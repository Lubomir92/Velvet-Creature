from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-me'

DEBUG = True

ALLOWED_HOSTS = []


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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================================================
# INTERNATIONALIZATION
# =========================================================

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = "en"

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

STATIC_URL = "/static/"

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

STRIPE_PUBLIC_KEY = "pk_test_51To46YRKljWp2kpVP7x9H293QXL0ynurZjdH13fwhVk60nxf1ykySSVv9KY9OjkyFjLnkccaDRbU8GaI6bxtXMLN00N5EGSMBU"

STRIPE_SECRET_KEY = "sk_test_51To46YRKljWp2kpVcKbbIb7XwThCQYSDDLqgP0Dtn2Wz98jXjHCacrQCGBzw2spUF6jbPfoyHq465tcWoDZiUgz600NaCMglFE"

STRIPE_WEBHOOK_SECRET = "whsec_013b34afc8aa6782df1fc00ab323a4a13955f763c4b4fd4b0b30e486793a5fa0"


# =========================================================
# EMAIL
# =========================================================



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DEFAULT_FROM_EMAIL = (
    "Velvet Creature <noreply@velvetcreature.com>"
)


DEFAULT_ADMIN_EMAIL = (
    "tvoj_email@example.com"
)


# =========================================================
# DEFAULT
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"