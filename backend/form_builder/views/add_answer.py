from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import Form, FormItem, Visitor, VisitorAnswer
from form_builder.serializers import AddVisitorAnswer


class AddAnswerView(APIView):
    def post(self, request: Request):
        try:
            form_id = request.data["form_id"]
            form_item_id = request.data["form_item_id"]
            visitor_id = request.data["visitor_id"]
            answer = request.data["answer"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        form = get_object_or_404(Form, id=form_id)
        form_item = get_object_or_404(FormItem, id=form_item_id)
        visitor = get_object_or_404(Visitor, id=visitor_id)

        if form_item.form_id != form.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            visitor_answer = VisitorAnswer.objects.create(
                form=form,
                form_item=form_item,
                visitor=visitor,
                answer=answer,
            )
        except IntegrityError:
            visitor_answer = VisitorAnswer.objects.get(
                form=form,
                form_item=form_item,
                visitor=visitor,
            )
            visitor_answer_srz = AddVisitorAnswer(instance=visitor_answer)
            return Response(status=status.HTTP_200_OK)

        visitor_answer_srz = AddVisitorAnswer(instance=visitor_answer)
        return Response(status=status.HTTP_201_CREATED)
