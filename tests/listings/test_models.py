from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from freezegun import freeze_time

from django_test_project.apps.listings import constants as listings_constants
from django_test_project.apps.listings.factories import ActiveListingFactory, ListingFactory
from django_test_project.apps.listings.models import Listing


class ListingQuerysetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.draft_listing_1 = ListingFactory()

        cls.unpublished_listing_1 = ListingFactory(
            status=listings_constants.LISTING_STATUS_UNPUBLISHED
        )

        cls.active_listing_1 = ActiveListingFactory()
        cls.active_listing_2 = ActiveListingFactory()

    def test_active(self):
        """
        Test the `active` queryset method.

        In this test, we should not retrieve any draft / unpublished listings.
        """
        results = list(Listing.objects.active())

        self.assertEqual(2, len(results))
        self.assertListEqual(
            results, [self.active_listing_1, self.active_listing_2],
        )


@freeze_time("2012-01-14 03:21:34")
class ListingTestCase(TestCase):
    def test_listing_draft_validation(self):
        """Perform validation tests on listing drafts."""
        # We should be able to create a draft ...
        listing = ListingFactory()
        self.assertIsNone(listing.published_at)
        self.assertEqual(listing.status, listings_constants.LISTING_STATUS_DRAFT)

        # ... but we should not be able to save an unpublished listing with a publication
        # date.
        listing.published_at = timezone.now()
        with self.assertRaises(ValidationError):
            listing.save()

    def test_listing_published_validation(self):
        """Perform validation tests on published listings."""
        listing = ActiveListingFactory()
        self.assertEqual(listing.published_at, timezone.now())
        self.assertEqual(listing.status, listings_constants.LISTING_STATUS_PUBLISHED)
