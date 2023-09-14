from rest_framework import serializers
from form_builder.models import Visitor, VisitorAnswer, Form, FormItem, VisitorForm


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


class FormSerializer(serializers.ModelSerializer):
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
            "category",
            "tags",
            "form_items",
        ]


class VisitorAnswersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VisitorAnswer
        fields = ["id", "visitor", "form", "form_item", "answer"]


class VisitorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    visitor_answers = serializers.SerializerMethodField()

    def get_visitor_answers(self, *args, **kwargs):
        if (
            self.context.get("form") is not None
            and self.context.get("visitor") is not None
        ):
            visitor_answers = VisitorAnswer.objects.filter(
                form=self.context["form"], visitor=self.context["visitor"]
            )
            visitor_answers_srz = VisitorAnswersSerializer(
                instance=visitor_answers, many=True
            )
            return visitor_answers_srz.data
        return VisitorAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Visitor
        fields = [
            "id",
            "auth_type",
            "auth_value",
            "visitor_answers",
        ]


class VisitorFormSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = VisitorForm
        fields = ["form", "visitor"]
