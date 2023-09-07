from django.db import models
from django.utils.translation import gettext as _

from backend.core.models import BaseModel
from backend.core.custom_manager import CustomManager


class SoftDeleteModel(BaseModel):
    """
    Abstract base model for soft-deleting records.
    """
    is_active = models.BooleanField(
        verbose_name=_('is_active'),
        default=True,
    )

    objects = CustomManager()

    def delete(self, using=None, keep_parents=False) -> None:
        """
        Soft deletes the model instance.
        """
        self.is_active = False
        self.save()

    class Meta:
        """
        This class defines metadata options for the SoftDeleteModel model.
        """
        abstract = True
