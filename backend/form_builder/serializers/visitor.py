from rest_framework import serializers
from backend.form_builder.models.form import Form
from backend.form_builder.models.form_item import FormItemModel


class FormItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormItemModel
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    form_items = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = '__all__'

    def get_form_items(self, obj):
        form_items = obj.form_items.all()
        return FormItemSerializer(instance=form_items, many=True)
