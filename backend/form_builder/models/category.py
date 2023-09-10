from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel, CreatedAtStampMixin


class Category(BaseModel, CreatedAtStampMixin):
    title = models.CharField(
        verbose_name=_("Title"), max_length=100, help_text=_("Please Enter title")
    )
    description = models.TextField(
        verbose_name=_("Description"), help_text=_("Please Enter description")
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Category"), _("Categories")
        db_table = "Category"

    def __str__(self):
        return self.title


class CategoryRecycle(Category):
    objects = models.Manager()

    class Meta:
        proxy = True
