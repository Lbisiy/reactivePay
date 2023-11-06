from django.urls import path
from .views import CallbackView

app_name = 'callback'

urlpatterns = [
    path('', CallbackView.as_view(), name='callback'),
]
