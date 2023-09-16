from rest_framework import serializers
from form_builder.models import VisitorAnswer


class UpdateAnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VisitorAnswer
        fields = ["id", "visitor", "form", "form_item", "answer"]
