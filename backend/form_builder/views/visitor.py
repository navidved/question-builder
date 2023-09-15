from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import Form, FormItem, Visitor, VisitorForm, VisitorAnswer
from form_builder.serializers.visitor import (
    FormSerializer,
    VisitorSerializer,
    VisitorFormSerializer,
    VisitorAnswersSerializer,
)


class GettingFormToAnswerView(APIView):
    def get(self, request: Request, form_slug):
        form = get_object_or_404(Form, slug=form_slug)
        form_srz = FormSerializer(instance=form)
        return Response(data=form_srz.data, status=status.HTTP_200_OK)


class VisitorAuthenticationView(APIView):
    def post(self, request):
        try:
            form_id = request.data["form"]
            auth_value = request.data["auth_value"]
            auth_type = request.data["auth_type"]

            form = Form.objects.get(id=form_id)
            visitor = Visitor.objects.get(auth_value=auth_value)
            visitor_form = VisitorForm.objects.get(form=form, visitor=visitor)
            visitor_form_srz = VisitorFormSerializer(
                instance=visitor_form, context={"form": form, "visitor": visitor}
            )
            return Response(data=visitor_form_srz.data, status=status.HTTP_200_OK)

        except Visitor.DoesNotExist:
            visitor_srz = VisitorSerializer(data=request.data, context={"form": form})
            visitor_srz.is_valid(raise_exception=True)
            visitor = visitor_srz.save()
            visitor_form = VisitorForm.objects.create(form=form, visitor=visitor)
            visitor_form_srz = VisitorFormSerializer(
                instance=visitor_form, context={"form": form, "visitor": visitor}
            )
            return Response(data=visitor_form_srz.data, status=status.HTTP_201_CREATED)

        except VisitorForm.DoesNotExist:
            visitor_form = VisitorForm.objects.create(form=form, visitor=visitor)
            visitor_form_srz = VisitorFormSerializer(
                instance=visitor_form, context={"form": form, "visitor": visitor}
            )
            return Response(data=visitor_form_srz.data, status=status.HTTP_201_CREATED)

        except (KeyError, Form.DoesNotExist):
            return Response(
                {"Error": "Invalid data provided"}, status=status.HTTP_400_BAD_REQUEST
            )


class AddVisitorAnswerView(APIView):
    def post(self, request: Request):
        try:
            form_id = request.data["form"]
            form_item_id = request.data["form_item"]
            visitor_id = request.data["visitor"]
            answer = request.data["answer"]
        except KeyError:
            return Response(
                {"Error": "Invalid data provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        form = get_object_or_404(Form, id=form_id)
        form_item = get_object_or_404(FormItem, id=form_item_id)
        visitor = get_object_or_404(Visitor, id=visitor_id)

        if form_item.form_id != form.id:
            return Response(
                {"Error": "Invalid data provided"}, status=status.HTTP_400_BAD_REQUEST
            )

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
            visitor_answer_srz = VisitorAnswersSerializer(instance=visitor_answer)
            data = {"message": "Already answered.", "data": visitor_answer_srz.data}
            return Response(data, status=status.HTTP_200_OK)

        visitor_answer_srz = VisitorAnswersSerializer(instance=visitor_answer)
        return Response(data=visitor_answer_srz.data, status=status.HTTP_201_CREATED)


class UpdateVisitorAnswerView(APIView):
    def patch(self, request: Request, answer_id):
        answer = get_object_or_404(VisitorAnswer, id=answer_id)
        answer_srz = VisitorAnswersSerializer(
            instance=answer, data=request.data, partial=True
        )
        if answer_srz.is_valid():
            answer_srz.save()
            data = {"message": "Answer Updated successfully.", "data": answer_srz.data}
            return Response(data, status=status.HTTP_200_OK)
        return Response(answer_srz.errors, status=status.HTTP_400_BAD_REQUEST)
