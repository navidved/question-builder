from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from datetime import datetime
from core.models import (SoftDeleteModel,
                         CreatedAtStampMixin,
                         UpdatedAtStampMixin,
                         )
# from form_builder.models.tag import Tag
# from form_builder.models.category import Category


class Form(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())

    file = models.FileField(upload_to="/form-files/")
    background_image = models.FileField(upload_to="/form-background-image")

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='FormUser',
    )

    tag = models.ForeignKey(
        "Tag",
        on_delete=models.CASCADE,
        related_name="forms",
    )

    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="forms",
    )


class FormUser(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
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
