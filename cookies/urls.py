from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('page/', views.page2, name="page"),
    path('count/',views.countView,name="count"),
    path('',views.index),
    path('addItem/',views.addItem, name="addItem"),
    path('displayItems', views.displayCart)
]
