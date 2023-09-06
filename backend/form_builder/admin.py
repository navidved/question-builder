from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from form_builder.models import Form, FormUser
from models.visitor_answer import VisitorAnswer, VisitorAnswerRecycle


class FormUserInLine(admin.StackedInline):
    model = FormUser
    fields = (
        "is_active"
        "form",
        "user",
    )


class FormTagInLine(admin.StackedInline):
    model = FormUser
    fields = (
        "is_active"
        "form",
        "tag",
    )


# Reza
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_select_related = ["user", "tag", "category"]
    list_display = ("is_active",
                    "id",
                    "title",
                    "start_date",
                    "end_date",
                    "category",
                    "created_at",
                    "updated_at",
                    )

    list_display_links = ("title", "start_date", "end_date", "category")
    list_filter = ('is_active')
    ordering = ("-created_at", "updated_at")
    date_hierarchy = "created_at"
    readonly_fields = ('created_at', 'updated_at')

    inlines = (FormUserInLine, FormTagInLine)

    add_fieldsets = (
        (None, {"fields": ("title",)}),
        )

    fieldsets = (
        (None, {"fields": ("title",)}),
        (_("Duration"), {"fields": ("start_date", "end_date")}),
        (_("Category"), {"fields": ("category")}),
    )


# Registering models
@admin.register(VisitorAnswer)
class VisitorAnswerAdmin(admin.ModelAdmin):
    list_display = ('form','form_item','answer')
    search_fields = ('form_item__text','visitor_id')
    list_filter = ('form_item',)

    def delete_queryset(self, request, queryset):
        """
        Override the delete_queryset method to update the is_active field of the queryset.
        """
        queryset.update(is_active=False)
        

@admin.register(VisitorAnswerRecycle)
class VisitorAnswerAdmin(admin.ModelAdmin):
    list_display = ('form','form_item','answer')
    search_fields = ('form_item__text','visitor_id')
    list_filter = ('form_item',)
    actions = ('activate_visitoranswer',)

    def get_queryset(self, request):
        """
        Returns a queryset of inactive VisitorAnswerRecycle objects.
        """
        return VisitorAnswerRecycle.objects.filter(is_active=False)

    @admin.action(description='visitoranswer activated successfully')
    def activate_visitoranswer(self, request, queryset):
        """
        Activate the selected answers.
        """
        queryset.update(is_active=True)