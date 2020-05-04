from django.contrib import admin

from django_test_project.apps.listings.models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass
