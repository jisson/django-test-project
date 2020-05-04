from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_test_project.apps.common import models as common_models
from django_test_project.apps.listings import constants as listings_constants


class ListingQueryset(models.QuerySet):
    def active(self):
        """Filter only on active listings."""
        return self.filter(
            owner__is_active=True, status=listings_constants.LISTING_STATUS_PUBLISHED,
        )


class Listing(common_models.Timestampable):

    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="listings", null=False,
    )

    STATUS_CHOICES = (
        (listings_constants.LISTING_STATUS_DRAFT, _("Draft")),
        (listings_constants.LISTING_STATUS_PUBLISHED, _("Published")),
        (listings_constants.LISTING_STATUS_UNPUBLISHED, _("Unpublished")),
    )

    label = models.CharField(
        _("Label"),
        null=False,
        blank=False,
        max_length=125,
        help_text=_("The label of the listing."),
    )

    published_at = models.DateTimeField(
        _("Published at"),
        null=True,
        editable=False,
        default=None,
        help_text=_("When the listing was published."),
    )

    status = models.CharField(
        _("Status"),
        null=False,
        blank=False,
        choices=STATUS_CHOICES,
        default="draft",
        max_length=12,
    )

    objects = ListingQueryset.as_manager()

    class Meta:
        verbose_name = _("Listing")
        verbose_name_plural = _("Listings")

    def save(self, *args, **kwargs):
        # Validate the model before saving it into our database.
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        if self.status == listings_constants.LISTING_STATUS_DRAFT and self.published_at:
            raise ValidationError(
                {"published_at": _("Draft listings may not have a publication date.")}
            )
        if (
            self.status == listings_constants.LISTING_STATUS_PUBLISHED
            and not self.published_at
        ):
            self.published_at = timezone.now()
