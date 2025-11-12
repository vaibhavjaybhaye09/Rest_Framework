from django.urls import path
from expenses import views

urlpatterns = [
    path('transactions/', views.TransactionAPI.as_view()),
]