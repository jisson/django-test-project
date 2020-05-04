from rest_framework import serializers

from django_test_project.apps.listings import models as listings_models


class ListingSerializer(serializers.ModelSerializer):

    owner = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="users:listings_owner_details",
    )

    class Meta:
        model = listings_models.Listing
        exclude = ["updated_at"]
