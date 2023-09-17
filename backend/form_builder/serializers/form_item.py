from rest_framework import serializers
from form_builder.models import FormItem


class FormItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormItem
        fields = [
            "id",
            "answer_type",
            "title",
            "description",
            "order",
            "answer_condition",
            "file_name",
            "time_limit",
            "options",
        ]
