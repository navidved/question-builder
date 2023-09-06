from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from users.models import Account, AccountRecycle
from users.messages.admin_messages import AdminMessages


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """
    AccountAdmin class for managing the Account model.
    """
    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_superuser',
        'is_staff',
        'is_active',
        ]
    list_filter = [
        'username',
        'email',
    ]
    filter_horizontal = ()
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "first_name",
                "last_name",
                "email",
                'image',
                'bio',
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = [
        "last_login",
        "date_joined",
    ]

    def delete_queryset(self, request, queryset):
        """
        Override the delete_queryset method to update the is_active field of the queryset.
        """
        queryset.update(
            is_active=False,
        )


@admin.register(AccountRecycle)
class AccountAdmin(admin.ModelAdmin):
    """
    Admin class for managing the AccountRecycle model.
    """
    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_superuser',
        'is_staff',
        'is_active',
    ]
    list_filter = [
        'username',
        'email',
    ]
    filter_horizontal = ()
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "first_name",
                "last_name",
                "email",
                'image',
                'bio',
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    actions = [
        'activate_user',
    ]

    def get_queryset(self, request):
        """
        Returns a queryset of inactive AccountRecycle objects.
        """
        return AccountRecycle.objects.filter(
            is_active=False,
        )

    @admin.action(
        description=AdminMessages.USER_ACTIVATE_DESC
    )
    def activate_user(self, request, queryset):
        """
        Activate the selected users.
        """
        queryset.update(
            is_active=True,
        )
