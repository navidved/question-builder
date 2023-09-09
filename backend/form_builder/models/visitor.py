from django.db import models
from core.models import BaseModel,CreatedAtStampMixin


class Visitor(CreatedAtStampMixin, BaseModel):
    AUTHENTICATION_CHOICES = [
    ("AN", "Ananymous"),
    ("EM", "Email"),
    ("PH", "Phone number")
    ]
    auth_type = models.CharField(
        max_length = 2,
        choices = AUTHENTICATION_CHOICES,
        default = 'Anonymous')
    
    auth_value = models.CharField(
        max_length=20)

    def __str__(self) -> str:
        return str(self.id)
    