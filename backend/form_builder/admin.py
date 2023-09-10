from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django_json_widget.widgets import JSONEditorWidget

from .models import (
    Category,
    Tag,
    TagRecycle,
    Form,
    FormRecycle,
    FormTag,
    FormUser,
    FormItem,
    FormItemRecycle,
    Visitor,
    VisitorRecycle,
    VisitorAnswer,
    VisitorAnswerRecycle,
)


class FormUserInLine(admin.StackedInline):
    model = FormUser
    fields = (
        "form",
        "user",
    )
    extra = 1


class FormTagInLine(admin.StackedInline):
    model = FormTag
    fields = (
        "form",
        "tag",
    )
    extra = 1


# Reza
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    inlines = (FormUserInLine, FormTagInLine)

    prepopulated_fields = {"slug": ("title",)}

    list_display = (
        "id",
        "is_active",
        "category",
        "slug",
        "title",
        "start_date",
        "end_date",
    )

    list_display_links = [
        "category",
        "slug",
        "title",
        "start_date",
        "end_date",
    ]
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Category"), {"fields": ("category",)}),
        (_("General"), {"fields": ("title", "description", "slug")}),
        (_("Timing"), {"fields": ("start_date", "end_date", "time_limit")}),
        (_("Others"), {"fields": ("file_name", "image_name")}),
    )


# Reza
@admin.register(FormRecycle)
class FormAdmin(admin.ModelAdmin):
    inlines = (FormUserInLine, FormTagInLine)

    prepopulated_fields = {"slug": ("title",)}

    list_display = (
        "id",
        "is_active",
        "category",
        "slug",
        "title",
        "start_date",
        "end_date",
    )

    list_display_links = [
        "category",
        "slug",
        "title",
        "start_date",
        "end_date",
    ]
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Category"), {"fields": ("category",)}),
        (_("General"), {"fields": ("title", "description", "slug")}),
        (_("Timing"), {"fields": ("start_date", "end_date", "time_limit")}),
        (_("Others"), {"fields": ("file_name", "image_name")}),
    )

    def get_queryset(self, request):
        """
        Returns a queryset of inactive Form objects.
        """
        return FormRecycle.objects.filter(is_active=False)

    @admin.action(description="Activate selected forms")
    def activate_form(self, request, queryset):
        """
        Activate selected forms.
        """
        queryset.update(is_active=True)


@admin.register(FormItem)
class FormItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    list_display = (
        "title",
        "form",
        "answer_type",
        "description",
        "time_limit",
    )

    list_display_links = (
        "title",
        "form",
        "description",
        "time_limit",
    )
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Required"), {"fields": ("form", "answer_type")}),
        (_("General"), {"fields": ("order", "title", "description")}),
        (_("Options"), {"fields": ("answer_condition", "options")}),
        (_("Othes"), {"fields": ("time_limit", "file_name")}),
    )


@admin.register(FormItemRecycle)
class FormItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    list_display = (
        "title",
        "form",
        "answer_type",
        "description",
        "time_limit",
    )

    list_display_links = (
        "title",
        "form",
        "description",
        "time_limit",
    )
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Required"), {"fields": ("form", "answer_type")}),
        (_("General"), {"fields": ("order", "title", "description")}),
        (_("Options"), {"fields": ("answer_condition", "options")}),
        (_("Othes"), {"fields": ("time_limit", "file_name")}),
    )

    def get_queryset(self, request):
        """
        Returns a queryset of inactive FormItem objects.
        """
        return FormItemRecycle.objects.filter(is_active=False)

    @admin.action(description="Activate selected form items")
    def activate_form_item(self, request, queryset):
        """
        Activate selected form items.
        """
        queryset.update(is_active=True)


# Registering models
@admin.register(VisitorAnswer)
class VisitorAnswerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    list_display = ("form", "form_item", "answer")
    list_display_links = ("form", "form_item", "answer")
    search_fields = ("form_item__text", "visitor")
    list_filter = ("form_item",)

    fieldsets = (
        (_("Required"), {"fields": ("visitor", "form", "form_item")}),
        (_("Answer"), {"fields": ("answer",)}),
    )


@admin.register(VisitorAnswerRecycle)
class VisitorAnswerAdmin(admin.ModelAdmin):
    list_display = ("form", "form_item", "answer")
    list_display_links = ("form", "form_item", "answer")
    search_fields = ("form_item__text", "visitor")
    list_filter = ("form_item",)
    actions = ("activate_visitoranswer",)

    def get_queryset(self, request):
        """
        Returns a queryset of inactive VisitorAnswerRecycle objects.
        """
        return VisitorAnswerRecycle.objects.filter(is_active=False)

    @admin.action(description="Activate selected answers")
    def activate_visitoranswer(self, request, queryset):
        """
        Activate selected answers.
        """
        queryset.update(is_active=True)


@admin.register(Visitor)
class VsitorAdmin(admin.ModelAdmin):
    list_display = ("id", "auth_type", "auth_value")
    list_display_links = ("id", "auth_type", "auth_value")
    search_fields = ("auth_value",)
    list_filter = ("auth_value",)


@admin.register(VisitorRecycle)
class VsitorAdmin(admin.ModelAdmin):
    list_display = ("id", "auth_type", "auth_value")
    list_display_links = ("id", "auth_type", "auth_value")
    search_fields = ("auth_value",)
    list_filter = ("auth_value",)

    def get_queryset(self, request):
        """
        Returns a queryset of inactive Visitor objects.
        """
        return VisitorRecycle.objects.filter(is_active=False)

    @admin.action(description="Activate selected visitors")
    def activate_visitor(self, request, queryset):
        """
        Activate selected visitors.
        """
        queryset.update(is_active=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk", "title", "created_at"]
    list_filter = ["title"]
    search_fields = ["title", "description"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk", "title", "created_at"]
    list_filter = ["title"]
    search_fields = ["title", "description"]


@admin.register(TagRecycle)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk", "title", "created_at"]
    list_filter = ["title"]
    search_fields = ["title", "description"]

    def get_queryset(self, request):
        """
        Returns a queryset of inactive Tag objects.
        """
        return TagRecycle.objects.filter(is_active=False)

    @admin.action(description="Activate selected tags")
    def activate_tag(self, request, queryset):
        """
        Activate the selected tag.
        """
        queryset.update(is_active=True)
