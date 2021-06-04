from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from rest_framework.views import APIView



# Uploading a single file

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  permission_classes
from rest_framework.decorators import api_view
#Uploading a single file and applying all the  authentication provided by DRF
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def upload_file(request):
    # if request.user.is_anonymous:
    #     return HttpResponse(status=401)
    if request.method == 'POST':
        print("here", request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request, 'success.html')


from django.views.generic.edit import FormView
from .forms import FileFieldForm
from .models import FileUpload


# Uploading multiple files
class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload_multiple.html'  # Replace with your template.
    success_url = '/success/url/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                instance = FileUpload(user=request.user, file=f)
                instance.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


import base64
from rest_framework.response import Response
# File data base 64 encoded via JSON
import json


class Base64(APIView):
    def post(self, request):
        file = request.FILES['file_field']
        print(type(file))
        print(dir(file))
        encoded_data = file.read()
        # print(files[0])
        # data = request.data['encoded_data']  # {"encoded_data": "aGVsbG8="}


        decoded = base64.b64decode(encoded_data)

        f = open(r"updates/{user}/files/{filename}".format(user=request.user, filename=file), 'w')
        print("updates/{user}/files/{filename}".format(user=request.user, filename=file))
        f.write(str(decoded))
        f.close()
        # Error handlibg in the future
        return Response({
            'Decoded text ': decoded
        })
