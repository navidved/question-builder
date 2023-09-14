from django.urls import path

from . import views

app_name = 'form_builder'

urlpatterns = [
    path('create/', views.VisitorAuthenticationView.as_view(), name='create-visitor'),
    path('answer/', views.AddVisitorAnswerView.as_view(), name='add-answer'),
    path('answer/<int:answer_id>/', views.UpdateVisitorAnswerView.as_view(), name='update-answer'),
    path('<slug:form_slug>/', views.GettingFormToAnswerView.as_view(), name='get-form'),
]
