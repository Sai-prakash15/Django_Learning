import json

class CustomMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print("Before the view is executed")
        request = self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        print("After the view is executed")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        return None

    def process_request(self, request):
        if(request.method == "POST"):
            print(request.body)
            # body = json.loads(request.body)
            # print(body)
        return request

    def process_response(self, request, response):
        if (request.method == "GET"):
            print(dir(response))
            # print(response.data["results"])
            # print(response.results)
            # body = json.loads(response.results)
            # print(body)
        print('"The Dark Knight is the best superhero movie of all time"')

        return response