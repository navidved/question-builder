import random
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from form_builder.models import Tag, Category
from core.models import (
    BaseModel,
    SoftDeleteModel,
    CreatedAtStampMixin,
    UpdatedAtStampMixin,
)


class Form(SoftDeleteModel, CreatedAtStampMixin, UpdatedAtStampMixin):
    ANONYMOUS = _("anonymous")
    EMAIL = _("email")
    PHONE = _("phone")
    AUTH_CHOICES = [
        (ANONYMOUS, _("Anonymous")),
        (EMAIL, _("Email")),
        (PHONE, _("Phone number")),
    ]
    auth_method = models.CharField(
        verbose_name=_("Authentication method"),
        choices=AUTH_CHOICES,
        default=ANONYMOUS,
        max_length=255,
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )

    description = models.TextField(
        _("Description"),
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

    start_date = models.DateTimeField(
        verbose_name=_("Start date and time"),
        default=timezone.now,
    )

    end_date = models.DateTimeField(
        verbose_name=_("End date and time"),
        blank=True,
        null=True,
    )

    time_limit = models.PositiveIntegerField(
        verbose_name=_("Time limit in second"),
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
        related_name="forms",
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        through="FormTag",
    )

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Users"),
        through="FormUser",
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        max_length=55,
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


class FormUser(BaseModel, CreatedAtStampMixin):
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
        unique_together = ("form", "user")


class FormTag(BaseModel, CreatedAtStampMixin):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form_tags")

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tag_forms",
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Form tag"), _("Form tags")
        db_table = "FormTag"
        unique_together = ("form", "tag")


class FormRecycle(Form):
    objects = models.Manager()

    class Meta:
        proxy = True
