from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.recipes_view),
    # path('multiple/', views.FileFieldFormView.as_view()),

]
