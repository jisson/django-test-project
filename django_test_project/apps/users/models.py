from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from django_test_project.apps.listings import constants as listings_constants


class User(AbstractUser):
    objects = UserManager()


class ListingOwnerQueryset(models.QuerySet):
    def has_listings(self):
        return self.with_listings_count().filter(listings_count__gte=1)

    def with_listings_count(self):
        """Annotate the owner with its total listings number."""
        return self.annotate(listings_count=models.Count("listings", distinct=True,))

    def with_active_listings_count(self):
        """Annotate the owner with its total active listings number."""
        return self.annotate(
            active_listings_count=models.Count(
                "listings",
                distinct=True,
                filter=models.Q(
                    listings__status=listings_constants.LISTING_STATUS_PUBLISHED
                ),
            )
        )


class ListingOwnerManager(models.Manager):
    def get_queryset(self):
        """Users are considered as listings owner only if they have at least on listing."""
        qs = super().get_queryset()

        # Annotate with listings counts.
        qs = qs.with_listings_count()
        qs = qs.with_active_listings_count()

        # Only filter on listings owner.
        qs = qs.has_listings()
        return qs


class ListingOwner(User):
    """Proxy models representing users that have listings."""

    objects = ListingOwnerManager.from_queryset(ListingOwnerQueryset)()

    class Meta:
        proxy = True
