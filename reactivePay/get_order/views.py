import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class GetOrderView(View):
    MERCHANT_PRIVATE_KEY = '##########'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request, order_number):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        response = requests.get(f'{self.SANDBOX_URL}/api/v1/payments/order/{order_number}', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(order_number)
            return HttpResponse(f'<html><body><span>Order {data}</body></html>')
        else:
            return HttpResponse(
                f'<html><body><span>Something gone wrong: {response.status_code, response.text}</span></body></html>')
