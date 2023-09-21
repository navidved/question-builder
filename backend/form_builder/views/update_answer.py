from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from form_builder.models import VisitorAnswer
from form_builder.serializers import UpdateAnswerSerializer


class UpdateAnswerView(APIView):
    def patch(self, request: Request, answer_id):
        answer = get_object_or_404(VisitorAnswer, id=answer_id)
        context = request.data["answer_type"]
        answer_srz = UpdateAnswerSerializer(
            instance=answer,
            data=request.data,
            partial=True,
            context={"answer_type": context},
        )
        answer_srz.is_valid(raise_exception=True)
        answer_srz.update(answer, answer_srz.validated_data)
        return Response(status=status.HTTP_200_OK)