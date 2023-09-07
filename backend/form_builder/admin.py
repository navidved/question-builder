from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CategoryModel
from .models import TagModel
from .models import Form, FormUser, FormTag
from .models import Visitor
from .models import VisitorAnswer, VisitorAnswerRecycle


class FormUserInLine(admin.StackedInline):
    model = FormUser
    fields = (
        "form",
        "user",
    )


class FormTagInLine(admin.StackedInline):
    model = FormTag
    fields = (
        "form",
        "tag",
    )


# Reza
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):

    inlines = (FormUserInLine, FormTagInLine)

    list_display = (
        "id",
        "is_active",
        "category",
        "slug",
        "title",
        "start_date",
        "end_date",
        )

    list_display_links = (
        "category",
        "slug",
        "title",
        "start_date",
        "end_date"
        )
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related('category').\
            prefetch_related('users').\
            prefetch_related('tags')


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


@admin.register(Visitor)
class VsitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'auth_type','auth_value')
    search_fields = ('auth_value',)
    list_filter = ('auth_value',)

    
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']

