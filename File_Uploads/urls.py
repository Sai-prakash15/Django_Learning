from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.upload_file, name='File'),
    path('multiple/', views.FileFieldFormView.as_view(), name='Multiple_File'),

]