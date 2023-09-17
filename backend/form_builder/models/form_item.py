from tkinter import SINGLE
from django.db import models
from django.utils.translation import gettext_lazy as _

from form_builder.models import Form
from core.models import (
    SoftDeleteModel,
    CreatedAtStampMixin,
    UpdatedAtStampMixin,
)


class FormItem(SoftDeleteModel, CreatedAtStampMixin, UpdatedAtStampMixin):
    SINGLE_CHOICE = "single-choice"
    MULTI_CHOICE = "multi-choice"
    TEXT = "text"
    ANSWER_TYPE_CHOICES = [
        (SINGLE_CHOICE, _("Single choice")),
        (MULTI_CHOICE, _("Multi choice")),
        (TEXT, _("Text")),
    ]

    ANSWER_CONDITION_CHOICES = [
        (0, _("Not Required")),
        (1, _("Required")),
    ]
    form = models.ForeignKey(
        Form,
        verbose_name=_("form"),
        related_name="form_items",
        on_delete=models.CASCADE,
    )
    answer_type = models.CharField(
        choices=ANSWER_TYPE_CHOICES,
        default=TEXT,
        max_length=255,
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
        verbose_name=_("answer condition"),
        choices=ANSWER_CONDITION_CHOICES,
        default=0,
    )
    time_limit = models.PositiveIntegerField(
        verbose_name=_("time limit"), blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name, verbose_name_plural = _("Form Item"), _("Form Items")
        db_table = "FormItem"
        unique_together = ("form", "order")


class FormItemRecycle(FormItem):
    objects = models.Manager()

    class Meta:
        proxy = True
