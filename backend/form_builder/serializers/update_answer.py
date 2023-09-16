from rest_framework import serializers
from form_builder.models import VisitorAnswer
from form_builder.validators import answer_validator


class UpdateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorAnswer
        fields = ["id", "answer"]

    def validate_answer(self, value: dict):
        res = answer_validator(self.context.get("answer_type"), value)
        if res:
            return value
        raise serializers.ValidationError("Incorrect Answer")

    def update(self, instance: VisitorAnswer, validated_data: dict):
        # validated_data.pop('answer_type')
        instance.answer = validated_data.get("answer")
        instance.save()
        return instance
