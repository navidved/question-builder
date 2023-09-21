import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from form_builder.models import Form, Visitor, VisitorForm
from form_builder.serializers import VisitorSerializer, VisitorFormSerializer , CreateVisitorSerializer


class CreateVisitorView(APIView):
    def post(self, request):
        try:
            form_id = request.data['form_id']
            form = Form.objects.get(id=request.data['form_id'])
        except KeyError:
            return Response(data={"form_id": ["This field is required."]},
                            status=status.HTTP_400_BAD_REQUEST)
        except Form.DoesNotExist:
            return Response(data={"form_id": ["this form does not exist."]},
                            status=status.HTTP_404_NOT_FOUND)

        srz_data = CreateVisitorSerializer(data=request.data, context={"form_id": form_id})
        if srz_data.is_valid():

            try:
                visitor = Visitor.objects.get(auth_value=request.data['auth_value'])
                try:
                    visitor_form = VisitorForm.objects.get(visitor=visitor, form=form)
                except VisitorForm.DoesNotExist:
                    visitor.form.add(form)

            except Visitor.DoesNotExist:
                visitor = None

            if visitor:
                visitor_srz = CreateVisitorSerializer(
                    instance=request.data,
                    context={
                        "form_id": form_id,
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data, status=status.HTTP_200_OK)

            if visitor is None:
                visitor = srz_data.create(validated_data=srz_data.validated_data)
                visitor_srz = CreateVisitorSerializer(
                    instance=request.data,
                    context={
                        "form_id": form_id,
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data, status=status.HTTP_201_CREATED)

        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
