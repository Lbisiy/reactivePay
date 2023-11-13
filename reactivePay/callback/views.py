import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):
    list_of_callbacks = []

    def post(self, request):
        req_o = json.loads(request.body)
        self.list_of_callbacks.append(req_o)
        print(self.list_of_callbacks)
        return HttpResponse('Status is:%s' % (req_o['status']))

        # if request.method == 'POST':
        #     try:
        #         req_o = json.loads(request.body)
        #         with open('text.txt', 'a') as file:
        #             file.write(req_o)
        #         return HttpResponse(f'Status is:{req_o["status"]}')
        #     except json.JSONDecodeError:
        #         return HttpResponseBadRequest('Invalid JSON data')
        #     else:
        #         return HttpResponseBadRequest('Unsupported HTTP method')
