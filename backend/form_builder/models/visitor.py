from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, CreatedAtStampMixin, UpdatedAtStampMixin
from form_builder.models import Form


class Visitor(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):
    ANONYMOUS = _("anonymous")
    EMAIL = _("email")
    PHONE = _("phone")
    AUTHENTICATION_CHOICES = [
        (ANONYMOUS, _("Anonymous")),
        (EMAIL, _("Email")),
        (PHONE, _("Phone number")),
    ]
    auth_type = models.CharField(
        choices=AUTHENTICATION_CHOICES,
        default=ANONYMOUS,
        max_length=255,
    )

    auth_value = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    form = models.ManyToManyField(
        Form,
        verbose_name=_("Form"),
        through="VisitorForm",
    )

    def __str__(self):
        return str(self.auth_value)

    class Meta:
        verbose_name, verbose_name_plural = _("Visitor"), _("Visitors")
        db_table = "Visitor"


class VisitorForm(BaseModel, CreatedAtStampMixin):
    visitor = models.ForeignKey(
        Visitor,
        verbose_name=_("Visitor"),
        on_delete=models.CASCADE,
    )

    form = models.ForeignKey(
        Form,
        verbose_name=_("Form"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Visitor form"), _("Visitor forms")
        db_table = "VisitorForm"
        unique_together = ("visitor", "form")
