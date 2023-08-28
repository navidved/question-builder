from django.contrib import admin
from models import visitor_answer

# Register your models here.
@admin.register(visitor_answer)
class VisitorAnswerAdmin(admin.ModelAdmin):
    list_display = ['form','form_item','answer']
    search_fields = ['form_item__text','visitor_id']
    # list_filter = ['']
