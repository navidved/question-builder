from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager

from core.models import SoftDeleteModel, CreatedAtStampMixin, UpdatedAtStampMixin


class VisitorAnswer(SoftDeleteModel, CreatedAtStampMixin, UpdatedAtStampMixin):
    default_answers = {
        "multi-choice": None,
        "radio-button": None,
        "text": None,
    }

    visitor = models.ForeignKey(
        "form_builder.Visitor", on_delete=models.CASCADE, related_name="visitor_answers"
    )

    form = models.ForeignKey(
        "form_builder.Form", on_delete=models.CASCADE, related_name="answers"
    )

    form_item = models.ForeignKey(
        "form_builder.FormItem", on_delete=models.CASCADE, related_name="answers"
    )

    answer = models.JSONField(
        verbose_name=_("Answer"),
        default=default_answers,
    )

    def __str__(self) -> str:
        return str(self.answer)

    class Meta:
        verbose_name, verbose_name_plural = _("Visitor answer"), _("Visitor answers")
        db_table = "VisitorAnswer"
        unique_together = ("visitor", "form", "form_item", "answer")


class VisitorAnswerRecycle(VisitorAnswer):
    objects = Manager()

    class Meta:
        proxy = True
