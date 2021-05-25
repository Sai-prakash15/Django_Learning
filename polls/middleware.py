import json
from rest_framework.response import Response
from cryptography.fernet import Fernet
import cryptography
from Induction.settings import  key

urls = ["/new/"]
class CustomMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        print("Before the view is executed")
        encrypted = self.process_request(request)
        self.process_response(request,encrypted)
        response = self.get_response(request)
        print("After the view is executed")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        return None

    def process_request(self, request):
        if (request.path not in urls):
            return request
        print("PROCESS REQUEST")
        if(request.method == "POST"):
            print("Before encryption",request.body)
            encoded = request.body
            f = Fernet(key)
            encrypted = f.encrypt(encoded)
            print("After encryption",encrypted)

            # print(request.body)
            # body = json.loads(request.body)
            # print(body)
        return encrypted

    def process_response(self, request, encrypted):
        print("PROCESS RESPONSE")
        if (request.path not in urls):
            return
        if (request.method == "POST"):
            # print(response)
            # print(request.body)
            fernet = Fernet(key)
            decrypted = fernet.decrypt(encrypted)  # Here request.body should be encrypted
            print("After decryption",decrypted)
            # response = decrypted
            #print(dir(response))
            # print(response.data["results"])
            # print(response.results)
            # body = json.loads(response.results)
            # print(body)
        # print('"The Dark Knight is the best superhero movie of all time"')