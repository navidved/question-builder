from rest_framework import serializers
from form_builder.models import VisitorAnswer


class VisitorAnswersSerializer(serializers.ModelSerializer):
    form_item_id = serializers.SerializerMethodField(read_only=True)
    answer_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = VisitorAnswer
        fields = [
            'form_item_id',
            'answer_type',
            'answer',
        ]

    def get_answer_type(self, obj):
        return obj.form_item.answer_type

    def get_form_item_id(self, obj):
        return obj.form_item.id
