"""
Project: {{ cookiecutter.project_name }}

Development configuration.

For more information, the complete list of configuration variables is available in the official documentation here:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import env

# DEBUG:
# In development, DEBUG mode is enabled.
# https://docs.djangoproject.com/en/5.1/ref/settings/#debug
DEBUG = True

# Secret key for the Django installation. It is used for cryptographic signing
# and should be set to a unique and non-predictable value.
# https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-SECRET_KEY
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)

# ALLOWED_HOSTS:
# A list of strings representing domain/host names that this Django site can serve.
# It’s a security measure to prevent HTTP Host header attacks, which are possible even
# with many seemingly secure web server configurations.
# https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"]
)

# EMAIL
# Email configuration. By default, emails are displayed in the terminal.
# To set up an email backend, define the DJANGO_EMAIL_URL environment variable with the following values:
# - SMTP with SSL: smtp+ssl://USER:PASSWORD@HOST:PORT
# - SMTP with STARTTLS: smtp+tls://USER:PASSWORD@HOST:PORT
# - Console: consolemail://
# https://docs.djangoproject.com/en/5.1/ref/settings/
EMAIL_BACKEND = env.email(
    "DJANGO_EMAIL_URL",
    default="consolemail://",
)

# DJANGO-DEBUG-TOOLBAR
# The Django Debug Toolbar is a debugging tool that integrates with Django to
# display detailed information about requests, databases, templates, views,
# and many other aspects:
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# The debug toolbar will only display if your IP address is listed in Django's
# INTERNAL_IPS setting.
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# This dictionary contains all other configuration options for Django-Debug-Toolbar.
# Some options apply to the toolbar itself, while others are specific to certain panels.
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Disables the profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
