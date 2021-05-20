from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
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