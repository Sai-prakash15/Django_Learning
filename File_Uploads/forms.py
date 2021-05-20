from django.forms import ModelForm
from File_Uploads.models import FileUpload
class UploadFileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = "__all__"
