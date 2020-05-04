from rest_framework import serializers

from django_test_project.apps.users import models as users_models


class ListingOwnerSerializer(serializers.ModelSerializer):

    listings_count = serializers.IntegerField()
    active_listings_count = serializers.IntegerField()

    class Meta:
        model = users_models.ListingOwner
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            # Annotation fields.
            "listings_count",
            "active_listings_count",
        )
