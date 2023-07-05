from django.urls import path
from user.views import ListUserView, DetailUserView, TopMaxTransactionUsersView, TopSumTransactionUsersView

urlpatterns = [
    path('', ListUserView.as_view()),
    path('<int:pk>/', DetailUserView.as_view()),
    path('top-max/', TopMaxTransactionUsersView.as_view()),
    path('top-sum/', TopSumTransactionUsersView.as_view()),
]