import json
from rest_framework.response import Response
from cryptography.fernet import Fernet
import cryptography
from Induction.settings import key
from django.http import HttpResponse

urls = ["/new/"]


class CustomMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path not in urls):
            response = self.get_response(request)
            return response
        print("-----------Before the view is executed------------------")
        request = self.process_request(request)
        response = self.get_response(request)
        print("---------------After the view is executed----------------")
        response = self.process_response(request, response)
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print('----- Middleware view %s' % view_func.__name__)
    #     return view_func(request)

    def process_request(self, request):
        print("PROCESS REQUEST")
        if (request.method == "POST"):
            print("Before decryption", request.body)
            f = Fernet(key)

            decrypted = f.decrypt(request.body)
            print("After decryption", decrypted)
            request._body = decrypted
            # print(request.body)
            # body = json.loads(request.body)
            # print(body)
        return request

    def process_response(self, request, response):

        print("PROCESS RESPONSE")
        if (request.method == "POST"):
            print("Before encrypting response", response.data)
            fernet = Fernet(key)
            encrypted = fernet.encrypt(response.data.encode())  # Here request.body should be encrypted
            print("After encrypted response", encrypted)
            return HttpResponse(encrypted)
            # response = decrypted
            # print(dir(response))
            # print(response.data["results"])
            # print(response.results)
            # body = json.loads(response.results)
            # print(body)
        return response
        # print('"The Dark Knight is the best superhero movie of all time"')
