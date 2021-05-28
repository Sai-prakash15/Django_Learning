from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views import View


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')

        return render(request, self.template_name)


class FormAjax(View):
    template_name = 'form_ajax.html'

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')

        return render(request, self.template_name)
