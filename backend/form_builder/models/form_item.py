from django.db import models
from backend.core.models import (
    SoftDeleteModel,
    CreatedAtStampMixin,
    UpdatedAtStampMixin,
)
from django.utils.translation import gettext_lazy as _
from backend.form_builder.models import form


class FormItem(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
    RADIOBUTTON = "RB"
    MULTICHECK = "MC"
    TEXT = "TX"
    ANSWER_TYPE_CHOICES = [
        (RADIOBUTTON, "Radio button"),
        (MULTICHECK, "Multi check"),
        (TEXT, "Text"),
    ]

    ANSWER_CONDITION_CHOICES = [
        (0, "Not Required"),
        (1, "Required"),
    ]
    form = models.ForeignKey(form, verbose_name=_("form"), on_delete=models.CASCADE)
    answer_type = models.CharField(
        max_length=2,
        choices=ANSWER_TYPE_CHOICES,
        default=TEXT,
    )
    title = models.CharField(
        verbose_name=_("title"),
        max_length=100,
    )
    description = models.TextField(
        verbose_name=_("description"),
        blank=True,
        null=True,
    )
    file_name = models.CharField(
        verbose_name=_("file name"),
        max_length=100,
        blank=True,
        null=True,
    )
    options = models.JSONField(verbose_name=_("options"))
    order = models.PositiveIntegerField(verbose_name=_("order"))
    answer_condition = models.PositiveIntegerField(
        verbose_name=_("answer condition"), choices=ANSWER_CONDITION_CHOICES, default=0
    )
    time_limit = models.PositiveIntegerField(
        verbose_name=_("time limit"), blank=True, null=True
    )
