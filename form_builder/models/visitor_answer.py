from django.db import models
from core.models import SoftDeleteModel, CreatedAtStampMixin, UpdatedAtStampMixin
from django.utils.translation import gettext_lazy as _


class VisitorAnswer(CreatedAtStampMixin, UpdatedAtStampMixin, SoftDeleteModel):
    form = models.ForeignKey(
        'form_builder.Form', 
        on_delete=models.CASCADE, 
        related_name='form_answers')
    
    question = models.ForeignKey(
        'form_builder.FormItem', 
        on_delete=models.CASCADE, 
        related_name='question_answers')
    
    answer = models.JSONField(verbose_name=_("Answer"))
    
    def __str__(self) -> str:
        return f'{self.id}'
    

    
