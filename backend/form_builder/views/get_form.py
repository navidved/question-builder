from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import Form
from form_builder.serializers import GetFormSerializer


class GetFormView(APIView):
    def get(self, request: Request, form_slug):
        form = get_object_or_404(Form, slug=form_slug)
        form_srz = GetFormSerializer(instance=form)
        return Response(data=form_srz.data, status=status.HTTP_200_OK)
