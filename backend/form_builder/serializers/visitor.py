from rest_framework import serializers
from form_builder.models import Visitor, VisitorAnswer, Form, FormItem


class FormItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormItem
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    form_items = FormItemSerializer(many=True)

    class Meta:
        model = Form
        exclude = ("slug", "users")


class VisitorAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorAnswer
        fields = ["visitor", "form", "form_item", "answer"]


class VisitorSerializer(serializers.ModelSerializer):
    visitor_answers = VisitorAnswersSerializer(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Visitor
        fields = [
            "id",
            "auth_type",
            "auth_value",
            "form",
            "visitor_answers",
        ]
