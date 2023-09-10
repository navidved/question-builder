from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, CreatedAtStampMixin, UpdatedAtStampMixin
from form_builder.models import Form


class Visitor(BaseModel, CreatedAtStampMixin, UpdatedAtStampMixin):
    AUTHENTICATION_CHOICES = [
        ("AN", "Anonymous"),
        ("EM", "Email"),
        ("PH", "Phone number"),
    ]
    auth_type = models.CharField(
        max_length=2, choices=AUTHENTICATION_CHOICES, default="Anonymous"
    )

    auth_value = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    form = models.ForeignKey(
        Form,
        verbose_name=_("Form"),
        on_delete=models.CASCADE
        )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name, verbose_name_plural = _("Visitor"), _("Visitors")
        db_table = "Visitor"


class VisitorRecycle(Visitor):
    objects = models.Manager()

    class Meta:
        proxy = True
