import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import Form, Visitor, VisitorForm
from form_builder.serializers import VisitorSerializer, VisitorFormSerializer , VisitorAuthSerializer


class CreateVisitorView2(APIView):
    def post(self, request):
        try:
            form_id = request.data["form"]
            auth_value = request.data["auth_value"]
            auth_type = request.data["auth_type"]

            if auth_value == "":
                request.data["auth_value"] = uuid.uuid4().hex

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


class CreateVisitorView(APIView):
    def post(self, request):
        srz_data = VisitorAuthSerializer(data=request.data, context={"form_id": request.data['form_id']})
        if srz_data.is_valid():
            try:
                visitor = Visitor.objects.get(auth_value=request.data['auth_value'])
            except Visitor.DoesNotExist:
                visitor = None
            if visitor:
                visitor_srz = VisitorAuthSerializer(
                    instance=request.data,
                    context={
                        "form_id": request.data['form_id'],
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data)
            if visitor is None:
                visitor = srz_data.create(validated_data=srz_data.validated_data)
                visitor_srz = VisitorAuthSerializer(
                    instance=request.data,
                    context={
                        "form_id": request.data['form_id'],
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data)
        return Response(data=srz_data.errors)
