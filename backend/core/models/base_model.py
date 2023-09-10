from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """
    Base model for other models to inherit from.
    """
    class Meta:
        """
        This class defines metadata options for the BaseModel model.
        """
        abstract = True


class CreatedAtStampMixin(models.Model):
    """
    Mixin class to add a created_at field to a model.
    """
    created_at = models.DateTimeField(
        verbose_name=_('created_at'),
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class UpdatedAtStampMixin(models.Model):
    """
    Mixin class to add an updated_at field to a model.
    """
    updated_at = models.DateTimeField(
        verbose_name=_('updated_at'),
        auto_now=True,
    )

    class Meta:
        abstract = True
