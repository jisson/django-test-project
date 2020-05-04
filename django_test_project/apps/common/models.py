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

    # FIXME: Check if this is useful.
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # Set help texts here. It would be empty on derived class otherwise.
    #     created_at = self._meta.get_field('created_at')
    #     created_at.help_text = _("When this object was created.")
    #     updated_at = self._meta.get_field('updated_at')
    #     updated_at.help_text = _("When this object was last updated.")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            # Automatically setting the `updated_at` value each time we update the model.
            self.updated_at = timezone.now()

        super().save(*args, **kwargs)
