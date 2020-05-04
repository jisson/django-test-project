from .base import *

DEBUG = env.bool("DJANGO_DEBUG", default=True,)

ALLOWED_HOSTS.extend(["127.0.0.1", "localhost"])

# SECRET KEY
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.

SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY", default="xe$yqh_u@-0ve(qwfr_ufsabcl2pi*!pq1k4w5j3%1q4mu03%3",
)

# Installed apps.

INSTALLED_APPS += [
    "django_extensions",
]


# Django extensions
# -----------------

# Truncate sql queries to this number of characters.
# To disable truncation of sql queries use None.
SHELL_PLUS_PRINT_SQL_TRUNCATE = env.int("SHELL_PLUS_PRINT_SQL_TRUNCATE", None)
SHELL_PLUS = env.str("SHELL_PLUS", "ipython")
