import requests
from django.http import HttpResponse
from django.views import View


class BalanceView(View):
    MERCHANT_PRIVATE_KEY = '#######'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        payload = {
            'currency': 'USD'
        }
        response = requests.get(f'{self.SANDBOX_URL}/api/v1/balance', json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return HttpResponse(f'<html><body><span>Your balance {data["wallet"]["available"]}</body></html>')
        else:
            return HttpResponse(
                f'<html><body><span>Something gone wrong: {response.status_code, response.text}</span></body></html>')
