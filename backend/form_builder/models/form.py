import random
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from core.models import (
    BaseModel,
    SoftDeleteModel,
    CreatedAtStampMixin,
    UpdatedAtStampMixin,
)
from form_builder.models import Tag, Category


class Form(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)

    description = models.TextField(_("Description"), blank=True, null=True)

    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        max_length=55,
    )

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
        through="FormUser",
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        through="FormTag",
    )

    category = models.ForeignKey(
        Category,
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

    class Meta:
        verbose_name, verbose_name_plural = _("Form"), _("Forms")
        db_table = "Form"


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

    class Meta:
        verbose_name, verbose_name_plural = _("Form user"), _("Form users")
        db_table = "FormUser"


class FormTag(CreatedAtStampMixin, UpdatedAtStampMixin, BaseModel):
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="forms",
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Form Tag"), _("Form Tags")
        db_table = "FormTag"


class FormRecycle(Form):
    objects = models.Manager()

    class Meta:
        proxy = True
