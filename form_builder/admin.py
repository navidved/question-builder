from django.contrib import admin
from models.visitor_answer import VisitorAnswer, VisitorAnswerRecycle

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