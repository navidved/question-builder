import json
import pytest

from model_bakery import baker
from rest_framework import status

from form_builder.models import (
    Form,
    FormItem,
)


@pytest.mark.django_db
class TestVisitor:
    def test_if_form_slug_not_valid_return_404(self, api_client):
        response = api_client.get("/api/visitor/form/zxljbcahsvckhavscljugoaecasc/")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_form_slug_is_valid_return_200(self, api_client):
        expected_form = {
            "id": 1,
            "auth_method": "AN",
            "title": "TestForm",
            "description": "TestFormDes.",
            "file_name": "aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
            "image_name": "aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
            "start_date": "2023-09-17T05:31:48.530000Z",
            "end_date": "2023-09-17T05:31:48.530000Z",
            "time_limit": 0,
            "form_items": [
                {
                    "id": 1,
                    "answer_type": "MC",
                    "title": "string",
                    "description": "string",
                    "order": 1,
                    "answer_condition": 0,
                    "file_name": "aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
                    "time_limit": 0,
                    "options": {
                        "multi-choice": ["string", "string2"],
                        "single-choice": ["string", "string2"],
                        "text": "string",
                    },
                }
            ],
        }
        form = baker.make(
            Form,
            auth_method="AN",
            title="TestForm",
            description="TestFormDes.",
            file_name="aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
            image_name="aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
            start_date="2023-09-17T05:31:48.530Z",
            end_date="2023-09-17T05:31:48.530Z",
            time_limit=0,
        )
        form_item = baker.make(
            FormItem,
            form_id=form.id,
            answer_type="MC",
            title="string",
            description="string",
            order=1,
            answer_condition=0,
            file_name="aa4aaa2c-c6ca-d5f5-b8b2-0b5c78ee2cb7",
            time_limit=0,
            options={
                "multi-choice": ["string", "string2"],
                "single-choice": ["string", "string2"],
                "text": "string",
            },
        )

        response = api_client.get(f"/api/visitor/form/{form.slug}/")

        assert response.status_code == status.HTTP_200_OK
        print(json.loads(response.content))
        print(expected_form)
        assert json.loads(response.content) == expected_form
