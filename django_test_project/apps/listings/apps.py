from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ListingsConfig(AppConfig):
    name = "django_test_project.apps.listings"
    verbose_name = _("Listings")
