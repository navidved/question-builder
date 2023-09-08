from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    form_items = serializers.SerializerMethodField()

    class Meta:
        model = FormModel
        fields = '__all__'

    def get_form_items(self, obj):
        form_items = obj.form_items.all()
        return FormItemSerializer(instance=form_items, many=True)
