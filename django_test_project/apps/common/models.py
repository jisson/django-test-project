from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Timestampable(models.Model):
    """
    Abstract models with a creation and modification date and time.
    """

    created_at = models.DateTimeField(
        _("Creation date"),
        editable=False,
        default=timezone.now,
        help_text=_("When this object was created."),
    )
    updated_at = models.DateTimeField(
        _("Last update date"),
        editable=False,
        default=timezone.now,
        help_text=_("When this object was last updated."),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            # Automatically setting the `updated_at` value each time we update the model.
            self.updated_at = timezone.now()

        super().save(*args, **kwargs)
