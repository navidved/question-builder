from rest_framework import serializers
from form_builder.models import VisitorAnswer
from form_builder.validators import answer_validator


class AddVisitorAnswerSerializer(serializers.ModelSerializer):
    def validate_answer(self, answer: dict):
        answer_type_validation = answer_validator(
            self.context.get("answer_type"),
            answer,
        )
        if answer_type_validation:
            return answer
        raise serializers.ValidationError("Incorrect Answer")

    class Meta:
        model = VisitorAnswer
        fields = [
            "form",
            "form_item",
            "visitor",
            "answer",
        ]
