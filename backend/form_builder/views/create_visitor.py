import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from form_builder.models import Form, Visitor, VisitorForm
from form_builder.serializers import VisitorSerializer, VisitorFormSerializer , CreateVisitorSerializer


class CreateVisitorView(APIView):
    def post(self, request):
        srz_data = CreateVisitorSerializer(data=request.data, context={"form_id": request.data['form_id']})
        if srz_data.is_valid():
            try:
                visitor = Visitor.objects.get(auth_value=request.data['auth_value'])
            except Visitor.DoesNotExist:
                visitor = None
            if visitor:
                visitor_srz = CreateVisitorSerializer(
                    instance=request.data,
                    context={
                        "form_id": request.data['form_id'],
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data)
            if visitor is None:
                visitor = srz_data.create(validated_data=srz_data.validated_data)
                visitor_srz = CreateVisitorSerializer(
                    instance=request.data,
                    context={
                        "form_id": request.data['form_id'],
                        "visitor_id": visitor.id,
                    }
                )
                return Response(data=visitor_srz.data)
        return Response(data=srz_data.errors)
