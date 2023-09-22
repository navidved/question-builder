from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import Form, FormItem, Visitor, VisitorAnswer
from form_builder.serializers import AddVisitorAnswerSerializer


class AddAnswerView(APIView):
    def post(self, request: Request):
        try:
            data = {
                "form": request.data["form_id"],
                "form_item": request.data["form_item_id"],
                "visitor": request.data["visitor_id"],
                "answer_type": request.data["answer_type"],
                "answer": request.data["answer"],
            }
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        form = get_object_or_404(Form, id=data["form"])
        form_item = get_object_or_404(FormItem, id=data["form_item"])
        visitor = get_object_or_404(Visitor, id=data["visitor"])

        if form_item.form_id != form.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if existed_answer := VisitorAnswer.objects.filter(
            form_id=form, visitor_id=visitor, form_item_id=form_item
        ):
            answer_type_data = {
                "id": existed_answer[0].id,
                "answer_type": data["answer_type"],
            }
            return Response(
                data=answer_type_data, status=status.HTTP_208_ALREADY_REPORTED
            )

        answer_type = data.pop("answer_type")
        visitor_answer_srz = AddVisitorAnswerSerializer(
            data=data,
            context={"answer_type": answer_type},
        )
        visitor_answer_srz.is_valid(raise_exception=True)
        answered_item = visitor_answer_srz.save()
        return Response(
            data={"id": answered_item.id, "answer_type": answer_type},
            status=status.HTTP_201_CREATED,
        )
