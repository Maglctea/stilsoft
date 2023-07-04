from django.urls import path, include

from transaction.views import ListTransactionView

urlpatterns = [
    path('', ListTransactionView.as_view()),
    path('', ListTransactionView.as_view()),
]