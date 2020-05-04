from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from django_test_project.apps.users import factories as user_factories
from . import constants as listings_constants
from . import models as listings_models


class ListingFactory(DjangoModelFactory):

    owner = SubFactory(user_factories.ActiveListingOwnerFactory)
    label = Sequence(lambda n: "Listing %03d" % n)

    class Meta:
        model = listings_models.Listing


class ActiveListingFactory(ListingFactory):
    """Factory for active listings."""

    status = listings_constants.LISTING_STATUS_PUBLISHED
