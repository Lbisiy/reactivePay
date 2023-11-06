import requests
from django.http import HttpResponse
from django.views import View


class BalanceView(View):
    MERCHANT_PRIVATE_KEY = '1dab4b92513e63571052'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        payload = {
            'currency': 'USD'
        }
        resp = requests.get(f'{self.SANDBOX_URL}/api/v1/balance', json=payload, headers=headers)

        if resp.status_code == 200:
            data = resp.json()
            return HttpResponse(f'<html><body><span>Your balance {data["wallet"]["available"]}</body></html>')
        else:
            return HttpResponse(
                f'<html><body><span>Something gone wrong: {resp.status_code, resp.text}</span></body></html>')
