from rest_framework import serializers
from form_builder.models import Visitor, VisitorAnswer
from form_builder.serializers import UpdateAnswerSerializer


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
