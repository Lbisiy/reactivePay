import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class PayoutView(View):
    MERCHANT_PRIVATE_KEY = '1dab4b92513e63571052'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request):
        return render(request, 'payout/create_payout.html')

    def post(self, request):
        payload = {
            "amount": int(request.POST['amount']),
            "currency": request.POST['currency'],
            "orderNumber": "10001",
            "card": {
                "pan": request.POST['pan'],
                "expires": request.POST['expires']
            },
            "customer": {
                "email": request.POST['email'],
                "address": "test test",
                "ip": "127.0.0.1"
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        response = requests.post(f'{self.SANDBOX_URL}/api/v1/payouts', json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return HttpResponse(f"<html><body><span>{data['payout']['status']}</html></body></span>")
        else:
            return HttpResponse(
                f'<html><body><span>Something gone wrong: {response.status_code}</span>: {response.text}</body></html>')

