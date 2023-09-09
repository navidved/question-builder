from rest_framework import serializers
from backend.form_builder.models import (Visitor,
                                         VisitorAnswer,
                                         Form,
                                         FormItem)


class FormItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormItem
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    form_items = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = '__all__'

    def get_form_items(self, obj):
        form_items = obj.form_items.all()
        return FormItemSerializer(instance=form_items, many=True)


class VisitorAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorAnswer
        field = '__all__'


class VisitorSerializer(serializers.ModelSerializer):
    visitor_answers = serializers.SerializerMethodField()

    class Meta:
        model = Visitor
        fields = '__all__'

    def get_visitor_answers(self, obj):
        visitor_answers = obj.visitor_answers.all()
        return VisitorAnswersSerializer(instance=visitor_answers, many=True)
