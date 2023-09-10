from django.urls import path

from . import views

app_name = 'form_builder'

urlpatterns = [
    path('/<slug:form_slug>/', views.GettingFormToAnswerView.as_view(), name='get-form'),
    path('create/', views.VisitorAuthenticationView.as_view(), name='create-visitor'),
    path('answer/', views.AddVisitorAnswer.as_view(), name='add-answer'),
    path('answer/<int:visitoranswer_id>/', views.AnswerUpdateView.as_view(), name='update-answer'),
]
