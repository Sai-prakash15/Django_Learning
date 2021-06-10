from django.urls import path, include
from . import views

urlpatterns = [
    path('count/',views.pageCount,name="count"),
    path('', views.index),
    path('addItem/', views.addItem, name="addItem"),
    path('displayItems/', views.displayCart)
]
