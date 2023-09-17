from rest_framework import serializers
from form_builder.models import VisitorAnswer
from form_builder.validators import answer_validator


class AddVisitorAnswerSerializer(serializers.ModelSerializer):
    def validate_answer(self, answer: dict):
        valid_answer = answer_validator(
            self.context.get("answer_type"),
            answer,
        )
        if valid_answer:
            return valid_answer
        raise serializers.ValidationError("Incorrect Answer")

    class Meta:
        model = VisitorAnswer
        fields = [
            "form",
            "form_item",
            "visitor",
            "answer",
        ]
