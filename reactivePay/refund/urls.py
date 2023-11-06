from django.urls import path
from .views import RefundView

app_name = 'refund'

urlpatterns = [
    path('', RefundView.as_view(), name='refund')
]
