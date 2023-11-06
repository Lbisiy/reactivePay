from django.urls import path
from .views import PayoutView

app_name = 'payout'

urlpatterns = [
    path('', PayoutView.as_view(), name='payout')
]
