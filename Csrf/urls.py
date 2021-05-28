from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('ajax/', views.FormAjax.as_view(), name="FormAjax")
]
