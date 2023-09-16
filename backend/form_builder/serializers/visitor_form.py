from rest_framework import serializers
from form_builder.models import VisitorForm
from form_builder.serializers import VisitorSerializer


class VisitorFormSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorForm
        fields = [
            "form",
            "visitor",
        ]
