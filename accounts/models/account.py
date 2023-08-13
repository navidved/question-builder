from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db.models import Manager

from core.models import SoftDeleteModel
from core.custom_manager import AccountCustomManager


class Account(AbstractUser, SoftDeleteModel):
    """
    This model represents user accounts in the system.
    """
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
    )

    objects = AccountCustomManager()

    def __str__(self):
        """
        Returns the string representation of the Account instance.
        """
        return self.username

    class Meta:
        """
        This class defines metadata options for the Account model.
        """
        indexes = [
            models.Index(
                fields=[
                    'username',
                    'email',
                ],
            ),
        ]


class AccountRecycle(Account):
    """
    This model represents recycled user accounts.
    """
    objects = Manager()

    class Meta:
        """
        This class defines metadata options for the AccountRecycle model.
        """
        proxy = True
