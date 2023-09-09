import random
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from core.models import (BaseModel,
                         SoftDeleteModel,
                         CreatedAtStampMixin,
                         UpdatedAtStampMixin,
                         )
from form_builder.models import TagModel
from form_builder.models import CategoryModel


class Form(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):

    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        max_length=55,
        )

    title = models.CharField(verbose_name=_("Title"), max_length=255)

    description = models.TextField(_("Description"), blank=True, null=True)

    start_date = models.DateTimeField(
        verbose_name=_("Start date and time"),
        default=timezone.now,
        )

    end_date = models.DateTimeField(
        verbose_name=_("End date and time"),
        blank=True,
        null=True,
        )

    file_name = models.UUIDField(
        verbose_name=_("File name"),
        blank=True,
        null=True,
    )

    image_name = models.UUIDField(
        verbose_name=_("Image name"),
        blank=True,
        null=True,
    )

    time_limit = models.PositiveIntegerField(
        verbose_name=_("Time limit in second"),
        blank=True,
        null=True,
        )

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Users"),
        through='FormUser',
    )

    tags = models.ManyToManyField(
        TagModel,
        verbose_name=_("Tags"),
        through='FormTag',
    )

    category = models.ForeignKey(
        CategoryModel,
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
        related_name="forms",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            title = self.title
            random_number = random.randint(100000, 999999)
            combined = f"{title} - {random_number}"
            self.slug = slugify(combined)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FormUser(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):

    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forms",
        )


class FormTag(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):

    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        )

    tag = models.ForeignKey(
        TagModel,
        on_delete=models.CASCADE,
        related_name="forms",
        )
