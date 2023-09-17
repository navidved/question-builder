from rest_framework import serializers
from form_builder.models import VisitorAnswer


class AddVisitorAnswer(serializers.ModelSerializer):
    answer_type = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data.pop('answer_type', None)
        return super().create(validated_data)

    def validate_answer(self, answer):
        pass

    class Meta:
        model = VisitorAnswer
        fields = [
            'visitor_id',
            'form_id',
            'form_item_id',
            'answer_type',
            'answer',
        ]
