from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from backend.form_builder.serializers.visitor import FormSerializer
from backend.form_builder.models.form import Form


class GettingFormToAnswerView(APIView):
    def get(self, form_slug):
        form = get_object_or_404(Form, slug=form_slug)
        form_srz = FormSerializer(instance=form)
        return Response(data=form_srz.data, status=status.HTTP_200_OK)


