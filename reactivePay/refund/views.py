import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View


class RefundView(View):
    MERCHANT_PRIVATE_KEY = '1dab4b92513e63571052'
    SANDBOX_URL = 'https://business.reactivepay.com'

    def get(self, request):
        return render(request, 'refund/create_refund.html')

    def post(self, request):

        payload = {
            "token": request.POST['token payment'],
            "amount": int(request.POST['request amount'])
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.MERCHANT_PRIVATE_KEY}'
        }

        response = requests.post(f'{self.SANDBOX_URL}/api/v1/refunds', json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return HttpResponse(
                f"<html><body><span>{data['refund']['amount']}, {data['refund']['status']}</html></body></span>")
        else:
            return HttpResponse(f'<html><body><span>Something gone wrong: {response.status_code}</span></body></html>')
