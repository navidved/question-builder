from django.db import models
from core.models import SoftDeleteModel
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.db.models import Manager

class VisitorAnswer(SoftDeleteModel):
    visitor_id = models.UUIDField(
        verbose_name=_('VisitorID'),
        default=uuid4)
    
    form = models.ForeignKey(
        'form_builder.Form', 
        on_delete=models.CASCADE, 
        related_name='answers')
    
    form_item = models.ForeignKey(
        'form_builder.FormItem', 
        on_delete=models.CASCADE, 
        related_name='answers')
    
    answer = models.JSONField(
        verbose_name=_("Answer"))
    
    def __str__(self) -> str:
        return self.id

    
class VisitorAnswerRecycle(VisitorAnswer):
    objects = Manager()
    
    class Meta:
        proxy = True