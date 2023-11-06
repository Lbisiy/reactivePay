from django.urls import path
from .views import BalanceView


app_name = 'balance'

urlpatterns = [
    path('', BalanceView.as_view(), name='balance'),
]
