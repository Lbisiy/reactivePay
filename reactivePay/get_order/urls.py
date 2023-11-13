from django.urls import path
from .views import GetOrderView


app_name = 'get_order'

urlpatterns = [
    path('<int:order_number>/', GetOrderView.as_view(), name='get_order'),
]
