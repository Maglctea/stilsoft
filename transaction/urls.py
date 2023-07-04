from django.urls import path

from transaction.views import ListTransactionView, DetailTransactionView

urlpatterns = [
    path('', ListTransactionView.as_view()),
    path('<int:pk>/', DetailTransactionView.as_view()),
]