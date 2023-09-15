from django.urls import path
from . import views

app_name = "form_builder"

urlpatterns = [
    path("auth/", views.VisitorAuthenticationView.as_view(), name="create-visitor"),
    path("answer/create/", views.AddVisitorAnswerView.as_view(), name="add-answer"),
    path(
        "answer/update/<int:answer_id>/",
        views.UpdateVisitorAnswerView.as_view(),
        name="update-answer",
    ),
    path(
        "form/<slug:form_slug>/",
        views.GettingFormToAnswerView.as_view(),
        name="get-form",
    ),
]
