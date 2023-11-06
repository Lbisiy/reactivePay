import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class PayView(View):

    MERCHANT_PRIVATE_KEY = '1dab4b92513e63571052'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request):
        return render(request, "pay/create.html")

    def post(self, request):

        payload = {
            "product": request.POST['product'],
            "amount": int(request.POST['amount']),
            "currency": request.POST['currency'],
            "callbackUrl": "https://maratsafin.pythonanywhere.com",
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        response = requests.post(f'{self.SANDBOX_URL}/api/v1/payments', json=payload, headers=headers)

        if response.status_code == 200:
            resp_payload = response.json()
            return HttpResponseRedirect(resp_payload['processingUrl'])
        else:
            return HttpResponse(f'<html><body><span>Something gone wrong: {response.status_code}</span></body></html>')
