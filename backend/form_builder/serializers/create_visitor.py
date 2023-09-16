import re

from rest_framework import serializers
from django.core.validators import
from form_builder.models import Visitor, VisitorAnswer
from form_builder.serializers import UpdateAnswerSerializer


def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def validate_phone_number(phone_number):
    if not re.match(r"^(?:\+98|0)?9\d{9}$", phone_number):
        return False
    return True

class VisitorAnswersSerializer2(serializers.ModelSerializer):
    form_item = serializers.IntegerField(label='form_item_id')
    answer_type = serializers.SerializerMethodField()


    class Meta:
        model = VisitorAnswer
        fields = [
            'form_item',
            'answer_type',
            'answer',
        ]

    def get_answer_type(self, obj):
        return obj.answers.answer_type

class VisitorAuthSerializer(serializers.Serializer):
    form_id = serializers.IntegerField()
    auth_type = serializers.CharField(write_only=True)
    auth_value = serializers.CharField(write_only=True)
    visitor_id = serializers.IntegerField(read_only=True)
    visitor_answers = serializers.SerializerMethodField(read_only=True)

    def get_visitor_answers(self, obj):
        ...

    def create(self, validated_data):
        ...

    def validate_auth_type(self, value):
        valid_auth_type = ['AN', 'EM', 'PH']
        if value not in valid_auth_type:
            raise serializers.ValidationError('The auth_type is wrong.')
        return value

    def validate(self, data):

        if data['auth_type'] == 'EM':
            if not validate_email(data['auth_value']):
                raise serializers.ValidationError('The email is invalid.')
            return data

        elif data['auth_type'] == 'PH':
            if not validate_phone_number(data['auth_value']):
                raise serializers.ValidationError('The phone number is invalid')
            return data

        else:
            if not data['auth_value'] == '':
                raise serializers.ValidationError('the auth value is invalid')
            return data









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
            visitor_answers_srz = UpdateAnswerSerializer(
                instance=visitor_answers, many=True
            )
            return visitor_answers_srz.data
        return UpdateAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Visitor
        fields = [
            "id",
            "auth_type",
            "auth_value",
            "visitor_answers",
        ]
