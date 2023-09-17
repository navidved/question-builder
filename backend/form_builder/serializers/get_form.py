from rest_framework import serializers
from form_builder.models import Form
from form_builder.serializers import FormItemSerializer


class GetFormSerializer(serializers.ModelSerializer):
    form_items = FormItemSerializer(many=True)

    class Meta:
        model = Form
        fields = [
            "id",
            "auth_method",
            "title",
            "description",
            "file_name",
            "image_name",
            "start_date",
            "end_date",
            "time_limit",
            "form_items",
        ]
