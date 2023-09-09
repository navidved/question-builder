from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from backend.form_builder.serializers.visitor import FormSerializer, VisitorSerializer
from backend.form_builder.models.form import Form
from backend.form_builder.models.visitor import Visitor


class GettingFormToAnswerView(APIView):
    def get(self, request: Request, form_slug):
        form = get_object_or_404(Form, slug=form_slug)
        form_srz = FormSerializer(instance=form)
        return Response(data=form_srz.data, status=status.HTTP_200_OK)


class VisitorAuthenticationView(APIView):
    def post(self, request: Request):
        visitor = Visitor.objects.get(form_id=request.data['form_id'],
                                      auth_value=request.data['auth_value'])
        if not visitor:
            visitor_srz = VisitorSerializer(data=request.data)
            if visitor_srz.is_valid():
                visitor_srz.create(validated_data=visitor_srz.validated_data)
                return Response(data=visitor_srz.data, status=status.HTTP_201_CREATED)
            return Response(data=visitor_srz.errors, status=status.HTTP_400_BAD_REQUEST)

        visitor_srz = VisitorSerializer(instance=visitor)
        return Response(data=visitor_srz.data, status=status.HTTP_200_OK)









