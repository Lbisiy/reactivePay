from django.urls import path
from .views import PayView


app_name = 'pay'

urlpatterns = [
    path('', PayView.as_view(), name='pay'),
]
