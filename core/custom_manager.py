from django.db import models
from django.contrib.auth.models import UserManager


class SoftQuerySet(models.QuerySet):
    """
    QuerySet class for soft-deleting records.
    """
    def delete(self) -> None:
        """
        Soft deletes the queryset.
        :return: None
        """
        return self.update(
            is_active=False,
        )


class CustomManager(models.Manager):
    """
    Custom manager class for soft-deleting records.
    """
    def get_queryset(self) -> SoftQuerySet:
        """
        Returns the queryset for the manager, filtering out inactive records.
        :return: SoftQuerySet
        """
        return SoftQuerySet(
            self.model,
            self._db,
        ).filter(
            is_active=True,
        )


class AccountCustomManager(UserManager):
    """
    Custom manager class for the Account model.
    """
    def get_queryset(self) -> models.QuerySet:
        """
        Returns the queryset for the manager, filtering out inactive accounts.
        :return: QuerySet
        """
        return super().get_queryset().filter(
            is_active=True,
        )
