from django.forms import ModelForm
from File_Uploads.models import FileUpload

class UploadFileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = "__all__"

from django import forms

class FileFieldForm(forms.Form):
    user = forms.CharField()
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))