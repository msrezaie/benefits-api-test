"""
Django settings for benefits project.

Generated by 'django-admin startpro23030ject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import django_heroku
import os
from decouple import config
import dj_database_url
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "authentication.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "sesame.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "EXCEPTION_HANDLER": "benefits.views.drf_exception_handler",
}

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # optional, if django-simple-history package is used
    "unfold.contrib.simple_history",
    "authentication.apps.AuthConfig",
    "corsheaders",
    "screener.apps.ScreenerConfig",
    "programs.apps.ProgramsConfig",
    "configuration.apps.ConfigurationConfig",
    "integrations.apps.IntegrationsConfig",
    "translations.apps.TranslationsConfig",
    "validations.apps.ValidationsConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "phonenumber_field",
    "parler",
    "django_json_widget",
    "django_filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "benefits.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "benefits.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASS"),
        "HOST": config("DB_HOST", "localhost"),
    }
}

DATABASES["default"] = dj_database_url.parse("postgresql://mfb_db_sp91_user:ETqMWfPdxrafrF0vc59TeURA3kNPvxzv@dpg-csgg671u0jms7390gp2g-a/mfb_db_sp91")


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = (
    ("en-us", _("US English")),
    ("es", _("Spanish")),
    ("vi", _("Vietnamese")),
    ("fr", _("French")),
    ("am", _("Amharic")),
    ("so", _("Somali")),
    ("ru", _("Russian")),
    ("ne", _("Nepali")),
    ("my", _("Burmese")),
    ("zh", _("Chinese")),
    ("ar", _("Arabic")),
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True
PARLER_DEFAULT_ACTIVATE = True
PARLER_LANGUAGES = {
    None: (
        {"code": "en-us"},
        {"code": "es"},
        {"code": "vi"},
        {"code": "fr"},
        {"code": "am"},
        {"code": "so"},
        {"code": "ru"},
        {"code": "ne"},
        {"code": "my"},
        {"code": "zh"},
        {"code": "ar"},
    ),
    "default": {
        "fallbacks": ["en-us"],  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        # the default; let .active_translations() return fallbacks too.
        "hide_untranslated": True,
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CSRF_FAILURE_VIEW = "benefits.views.catch_403_view"

SWAGGER_SETTINGS = {"SUPPORTED_SUBMIT_METHODS": ("get",), "DEEP_LINKING": True}

# Enable logging with Sentry if it is enabled
if config("SENTRY_DSN", None) is not None:
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        environment="dev" if DEBUG else "production",
    )

django_heroku.settings(locals())


# UNFOLD SETTINGS
UNFOLD = {
    "SITE_HEADER": _("MFB Admin"),
    "SITE_TITLE": _("MFB Admin"),
    "APP_NAME": "Benefits",
    "APP_VERSION": "1.0.0",
    "APP_DESCRIPTION": "Benefits is a Django application that helps people find and apply for benefits.",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Navigation"),
                "items": [
                    {
                        "title": _("Programs"),
                        "icon": "other_admission",
                        "link": reverse_lazy("admin:programs_program_changelist"),
                    },
                    {
                        "title": _("Urgent Needs"),
                        "icon": "breaking_news",
                        "link": reverse_lazy("admin:programs_urgentneed_changelist"),
                    },
                    {
                        "title": _("Navigators"),
                        "icon": "near_me",
                        "link": reverse_lazy("admin:programs_navigator_changelist"),
                    },
                    {
                        "title": _("Warning Messages"),
                        "icon": "error",
                        "link": reverse_lazy("admin:programs_warningmessage_changelist"),
                    },
                    {
                        "title": _("Configurations"),
                        "icon": "tune",
                        "link": reverse_lazy("admin:configuration_configuration_changelist"),
                    },
                    {
                        "title": _("Translation Overrides"),
                        "icon": "letter_switch",
                        "link": reverse_lazy("admin:programs_translationoverride_changelist"),
                    },
                ],
            },
            {
                "separator": True,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Translations Admin"),
                        "icon": "settings",
                        "link": reverse_lazy("translations_api_url"),
                    },
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:authentication_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": _("Tokens"),
                        "icon": "key",
                        "link": reverse_lazy("admin:authtoken_tokenproxy_changelist"),
                    },
                ],
            },
        ],
    },
}

# generate uml with: ./manage.py graph_models --pydot
# adding -d will exclude the fields
GRAPH_MODELS = {
    "output": "./_mfb_uml.png",
    "group_models": True,
    "app_labels": ["screener", "programs", "configuration", "validations", "authentication"],
    "exclude_models": ["Translation"],
}
