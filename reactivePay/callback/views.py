import json

from django.http import HttpResponse
from django.views import View


class CallbackView(View):
    list_of_callbacks = []

    def post(self, request):

        try:
            notification_data = json.loads(request.read())

            token = notification_data.get('token')
            payment_type = notification_data.get('type')
            status = notification_data.get('status')
            extraReturnParam = notification_data.get('extraReturnParam')
            orderNumber = notification_data.get('orderNumber')
            walletToken = notification_data.get('walletToken')
            recurringToken = notification_data.get('recurringToken')
            sanitizedMask = notification_data.get('sanitizedMask')
            amount = notification_data.get('amount')
            currency = notification_data.get('currency')
            gatewayAmount = notification_data.get('gatewayAmount')
            gatewayCurrency = notification_data.get('gatewayCurrency')

            self.list_of_callbacks.append(notification_data)
            return HttpResponse('Status is:200')

        except json.JSONDecodeError:
            return HttpResponse('Status is:400')
