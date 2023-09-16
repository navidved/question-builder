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
        answer_srz = UpdateAnswerSerializer(
            instance=answer, data=request.data, partial=True
        )
        if answer_srz.is_valid():
            answer_srz.save()
            data = {"message": "Answer Updated successfully.", "data": answer_srz.data}
            return Response(data, status=status.HTTP_200_OK)
        return Response(answer_srz.errors, status=status.HTTP_400_BAD_REQUEST)
