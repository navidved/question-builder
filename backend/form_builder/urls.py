from django.urls import path
from . import views

app_name = "form_builder"

urlpatterns = [
    path("auth/", views.CreateVisitorView.as_view(), name="create-visitor"),
    path("answer/create/", views.AddAnswerView.as_view(), name="add-answer"),
    path(
        "answer/update/<int:answer_id>/",
        views.UpdateAnswerView.as_view(),
        name="update-answer",
    ),
    path(
        "form/<slug:form_slug>/",
        views.GetFormView.as_view(),
        name="get-form",
    ),
]
