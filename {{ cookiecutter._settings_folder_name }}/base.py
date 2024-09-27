"""
Project: {{ cookiecutter.project_name }}

Basic configuration common to all settings files.

For more information, the complete list of configuration variables is available in the official documentation here:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from . import BASE_DIR
from . import env

# DEBUG:
# By default, DEBUG mode is disabled to prevent accidental enablement in production.
# https://docs.djangoproject.com/en/5.1/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# ALLOWED_HOSTS:
# A list of strings representing domain/host names that this Django site can serve.
# This is a security measure to prevent HTTP Host header attacks, which are possible even
# with many seemingly secure web server configurations.
# https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Installed applications for this Django project
INSTALLED_APPS = [
    {%- if cookiecutter.use_wagtail %}
    # Wagtail applications
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail",
    "rest_framework",
    "modelcluster",
    "taggit",{% endif %}
    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    # External applications
    "django_extensions",
    # Add your own applications...
]

# MULTI-SITE MANAGEMENT
# The ID, as an integer, of the current site in the django_site database table.
# This is used to allow application data to associate with specific sites,
# and a single database can manage content for multiple sites.
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# MIDDLEWARE:
# Middleware is a system of hooks into Django’s request/response processing.
# It’s a lightweight, low-level plugin system for globally altering Django’s input or output.
# https://docs.djangoproject.com/en/5.1/ref/settings/#middleware
# You can learn how to write your own middleware here:
# https://docs.djangoproject.com/en/5.1/topics/http/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    {%- if cookiecutter.use_wagtail %}
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",{% endif %}
]

# URLS:
# A string representing the full Python import path to your root URLconf,
# for example "mydjangoproject.urls".
# https://docs.djangoproject.com/en/5.1/ref/settings/#root-urlconf
ROOT_URLCONF = "{{ cookiecutter.__config_dir }}.urls"

# TEMPLATES:
# A list containing the settings for all template engines to use with Django.
# Each item in the list is a dictionary containing the options for each engine.
# https://docs.djangoproject.com/en/5.1/ref/settings/#templates
TEMPLATES = [
    {
        # The template engine to use. Built-in Django template engines are:
        # - DjangoTemplates: 'django.template.backends.django.DjangoTemplates'
        # - Jinja2: 'django.template.backends.jinja2.Jinja2'
        # https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Directories where the engine looks for template source files, in the order given.
        # https://docs.djangoproject.com/en/5.1/ref/settings/#dirs
        "DIRS": [],
        # Indicates whether the engine should look for template source files inside installed applications.
        # https://docs.djangoproject.com/en/5.1/ref/settings/#app-dirs
        "APP_DIRS": True,
        # Additional options to pass to the template engine. Available options vary depending on the engine.
        "OPTIONS": {
            # List of context processors. Here’s what each built-in context processor does:
            # https://docs.djangoproject.com/en/5.1/ref/templates/api/#built-in-template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

# The full Python path of the WSGI application object that Django's built-in servers
# (e.g., runserver) will use.
# https://docs.djangoproject.com/en/5.1/ref/settings/#wsgi-application
WSGI_APPLICATION = "{{ cookiecutter.__config_dir }}.wsgi.application"

# DATABASE:
# A dictionary containing the settings for all databases to be used with Django.
# The DATABASES setting must configure a default database; you can define as many additional databases as needed.
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# This database configuration uses an environment variable in URL form named DJANGO_DATABASE_URL.
# Examples of such configuration URLs are:
# - POSTGRESQL: postgres://USER:PASSWORD@HOST:PORT/DB_NAME (with psycopg driver)
# - MYSQL: mysql://USER:PASSWORD@HOST:PORT/DB_NAME (with mysqlclient driver)
# - SQLITE: sqlite:///FILE_NAME (driver included by default in Python)
DATABASES = {
    "default": env.db(
        "DJANGO_DATABASE_URL",
        default="sqlite:///db.sqlite3"
    )
}

# Type of primary key field to use by default for models that don’t have a primary_key=True field.
# https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# PASSWORD VALIDATION
# A list of validators used to check the strength of user passwords.
# For more info on password validation:
# https://docs.djangoproject.com/en/5.1/topics/auth/passwords/#password-validation
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

# PASSWORD HASHING
# Configuration of password hashing.
# https://docs.djangoproject.com/en/5.1/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # Argon2 is not the default algorithm in Django because it requires an external library (argon2-cffi).
    # Password Hashing Competition experts recommend immediate use of Argon2 over other algorithms
    # supported by Django.
    # https://docs.djangoproject.com/en/5.1/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# INTERNATIONALIZATION
# The purpose of internationalization and localization is to allow a single web application
# to present its content in multiple languages and formats to suit different users.
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# A string representing the language code for this installation. It should conform to the standard
# language format.
# For example, US English is “en-us” or French is “fr”.
# You can also see the list of language identifiers here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# Documentation for LANGUAGE_CODE is here:
# https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-LANGUAGE_CODE
LANGUAGE_CODE = "{{ cookiecutter.language }}"

# A string representing the timezone for this installation.
# 'America/Chicago' is the default value, but the initial setting often uses 'UTC'.
# You can find a list of timezones here:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# For Paris, for example, you can use 'Europe/Paris'
TIME_ZONE = "{{ cookiecutter.timezone }}"

# A boolean value that specifies whether Django’s translation system should be enabled.
# It’s a way to turn it off to gain a slight performance improvement.
# If set to False, Django will make some optimizations so as not to load the translation mechanism.
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# A boolean value that specifies if datetimes should be timezone-aware. If set to True,
# Django will use timezone-aware datetimes internally.
# When USE_TZ is False, Django uses naive local datetimes unless ISO 8601 formatted datetimes
# with timezone information are parsed; in that case, the timezone is preserved.
# https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-USE_TZ
USE_TZ = True

# USER AUTHENTICATION
# A list of authentication backend classes (as strings) to use when attempting to authenticate a user.
# See the documentation on authentication backends for more details.
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#other-authentication-sources
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# The model to use for representing a user. See Substituting a custom User model.
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "{{ cookiecutter.user_model }}"

{%- if cookiecutter.login_redirect_url %}

# The URL or named URL pattern to redirect to after login if the LoginView view does not receive a GET parameter named 'next'.
# https://docs.djangoproject.com/en/5.1/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "home"{% endif %}

{%- if cookiecutter.logout_redirect_url %}

# The URL or named URL pattern to redirect to after logout if the LogoutView view does not have a 'next_page' attribute.
# https://docs.djangoproject.com/en/5.1/ref/settings/#logout-redirect-url
LOGOUT_REDIRECT_URL = "home"{% endif %}

# The URL or named URL pattern to redirect to for login with the login_required() decorator,
# the LoginRequiredMixin, AccessMixin, or when the LoginRequiredMiddleware is installed.
# https://docs.djangoproject.com/en/5.1/ref/settings/#login-url
LOGIN_URL = "{{ cookiecutter.login_url }}"

# STATIC FILES AND MEDIA (CSS, JavaScript, Images)
# Websites generally need to serve additional files such as images, JavaScript, or CSS.
# In Django, these files are called “static files”. Django provides the django.contrib.staticfiles app to help with this.
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# The absolute path to the directory where collectstatic will gather static files for deployment.
# https://docs.djangoproject.com/en/5.1/ref/settings/#static-root
STATIC_ROOT = Path(env("DJANGO_STATIC_ROOT", default=str(BASE_DIR / "staticfiles")))

# URL to use when referring to static files located in STATIC_ROOT.
# https://docs.djangoproject.com/en/5.1/ref/settings/#static-url
STATIC_URL = "/static/"

# This setting defines additional locations that the staticfiles app should traverse.
# https://docs.djangoproject.com/en/5.1/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = []

# The STORAGES configuration defines the storage backends for default files and static files in a Django application.
# https://docs.djangoproject.com/en/5.1/ref/settings/#storages
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# A list of static file storage engines that know how to find static files in various locations.
# https://docs.djangoproject.com/en/5.1/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA FILES

# Absolute path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/5.1/ref/settings/#media-root
MEDIA_ROOT = Path(env("DJANGO_MEDIA_ROOT", default=str(BASE_DIR / "media")))

# URL that handles the media served from MEDIA_ROOT, used for managing stored files.
# It should end with a slash if it’s not empty.
# https://docs.djangoproject.com/en/5.1/ref/settings/#media-url
MEDIA_URL = "/media/"

# SECURITY
# Indicates whether to use the HttpOnly flag on the session cookie.
# If set to True, client-side JavaScript will not be able to access the session cookie.
# https://docs.djangoproject.com/en/5.1/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# Indicates whether to use the HttpOnly flag on the CSRF cookie. If set to True,
# client-side JavaScript will not be able to access the CSRF cookie.
# https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False

# Default value for the X-Frame-Options header used by XFrameOptionsMiddleware
# to protect against clickjacking.
# https://docs.djangoproject.com/en/5.1/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# Email configuration. By default, emails are displayed in the terminal.
# To set up an email backend, define the DJANGO_EMAIL_URL environment variable with the following values:
# - SMTP with SSL: smtp+ssl://USER:PASSWORD@HOST:PORT
# - SMTP with STARTTLS: smtp+tls://USER:PASSWORD@HOST:PORT
# - Console: consolemail://
# https://docs.djangoproject.com/en/5.1/ref/settings/
EMAIL_CONFIG = env.email(
    "DJANGO_EMAIL_URL",
    default="consolemail://",
)
globals().update(**EMAIL_CONFIG)

# Sets a timeout in seconds for blocking operations such as attempting to connect.
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN EMAILS
# A list of all people who receive error notifications.
# When DEBUG=False and AdminEmailHandler is configured in LOGGING (default behavior),
# Django sends an email to these people with details of the exceptions raised in the request/response cycle.
# https://docs.djangoproject.com/en/5.1/ref/settings/#admins
ADMINS = [
    ("""{{ cookiecutter.author_name }}""", "{{ cookiecutter.email }}")
]

# A list in the same format as ADMINS that specifies who should receive broken link notifications
# when BrokenLinkEmailsMiddleware is enabled.
# https://docs.djangoproject.com/en/5.1/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# Logging configuration dictionary.
# Default values can be found here:
# https://github.com/django/django/blob/main/django/utils/log.py
# https://docs.djangoproject.com/en/5.1/ref/settings/#logging
# See also https://docs.djangoproject.com/en/5.1/topics/logging/ for more details on logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

{%- if cookiecutter.use_wagtail %}

# Wagtail settings

WAGTAIL_SITE_NAME = "{{ cookiecutter.project_name }}"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://127.0.0.1:8000"

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]{% endif %}
