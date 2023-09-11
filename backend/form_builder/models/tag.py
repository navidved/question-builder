from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, CreatedAtStampMixin


class Tag(BaseModel, CreatedAtStampMixin):
    title = models.CharField(
        unique=True,
        verbose_name=_("Title"),
        max_length=100,
        help_text=_("Please enter title"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Please enter description"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Tag"), _("Tags")
        db_table = "Tag"

    def __str__(self):
        return self.title
