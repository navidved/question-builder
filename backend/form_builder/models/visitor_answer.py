from django.db import models
from core.models import SoftDeleteModel
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager


class VisitorAnswer(SoftDeleteModel):
    default_answers = {
        "multi-choice": [
            "choice-1",
            "choice-2",
            "etc.",
        ],
        "radio-button": [
            "choice-1",
            "choice-2",
            "etc.",
        ],
        "text": "visitor-answer-text",
    }

    visitor_id = models.ForeignKey(
        "form_builder.Visitor", on_delete=models.CASCADE, related_name="answers"
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


class VisitorAnswerRecycle(VisitorAnswer):
    objects = Manager()

    class Meta:
        proxy = True
