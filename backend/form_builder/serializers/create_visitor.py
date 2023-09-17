import re
import uuid
from rest_framework import serializers
from form_builder.models import Visitor, VisitorAnswer, Form
from form_builder.validators.email import validate_email
from form_builder.validators.phone_number import validate_phone_number


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


class CreateVisitorSerializer(serializers.Serializer):
    form_id = serializers.IntegerField()
    auth_type = serializers.CharField(write_only=True)
    auth_value = serializers.CharField(write_only=True, allow_blank=True)
    visitor_id = serializers.SerializerMethodField(read_only=True)
    visitor_answers = serializers.SerializerMethodField(read_only=True)

    def get_visitor_id(self, *args):
        return self.context.get('visitor_id')

    def get_visitor_answers(self, obj):
        form = Form.objects.get(id=self.context.get('form_id'))
        visitor = Visitor.objects.get(id=self.context.get('visitor_id'))

        answers = VisitorAnswer.objects.filter(
            form=form, visitor=visitor
        )
        return VisitorAnswersSerializer(instance=answers, many=True).data

    def create(self, validated_data):
        if validated_data['auth_value'] == "":
            validated_data["auth_value"] = uuid.uuid4().hex
        visitor = Visitor.objects.create()
        visitor.auth_type = validated_data['auth_type']
        visitor.auth_value = validated_data['auth_value']
        visitor.save()
        form = Form.objects.get(id=validated_data['form_id'])
        visitor.form.add(form)
        return visitor

    def validate_auth_type(self, value):
        valid_auth_type = ['anonymous', 'email', 'phone']
        if value not in valid_auth_type:
            raise serializers.ValidationError('The auth_type is wrong.')
        return value

    def validate(self, data):

        if data['auth_type'] == 'email':
            if not validate_email(data['auth_value']):
                raise serializers.ValidationError('The email is invalid.')
            return data

        elif data['auth_type'] == 'phone':
            if not validate_phone_number(data['auth_value']):
                raise serializers.ValidationError('The phone number is invalid')
            return data

        if data['auth_value'] != '':
            raise serializers.ValidationError('anonymous error!')
        return data


