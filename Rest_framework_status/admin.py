from django.contrib import admin

# Register your models here.
from .models import Status
from .forms import StatusForm

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = StatusForm

admin.site.register(Status, StatusAdmin)