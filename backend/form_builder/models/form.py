from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from datetime import datetime
from core.models import (BaseModel,
                         SoftDeleteModel,
                         CreatedAtStampMixin,
                         UpdatedAtStampMixin,
                         )
from form_builder.models import Tag
from form_builder.models import Category


class Form(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        )
    start_date = models.DateTimeField(
        blank=True,
        null=True,
        default=datetime.now(),
        )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        default=datetime.now(),
        )

    file = models.UUIDField(
        blank=True,
        null=True,
    )
    background_image = models.UUIDField(
        blank=True,
        null=True,
    )

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='FormUser',
    )

    tag = models.ManyToManyField(
        Tag,
        through='FormTag',
    )

    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
        related_name="forms",
    )


class FormUser(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_forms",
        )

    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name="form_users",
        )


class FormTag(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tag_forms",
        )

    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name="form_tags",
        )
