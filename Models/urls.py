from django.urls import path, include, re_path
from django.conf.urls import url
from .views import Scenario1, Scenario2, Scenario3, Scenario4, Scenario5, Scenario6, Scenario7, Scenario8, Scenario9, \
    Scenario10, Scenario11, Scenario11_1, Scenario11_2
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

# router.register('scenario1', Scenario1)
#
#
# urlpatterns = [
#     path('',include(router.urls)),
# ]

urlpatterns = [
    path('scenario1/', Scenario1.as_view()),
    path('scenario2/', Scenario2.as_view()),
    path('scenario3/', Scenario3.as_view()),
    path('scenario4/', Scenario4.as_view()),
    path('scenario5/', Scenario5.as_view()),
    path('scenario6/', Scenario6.as_view()),
    path('scenario7/', Scenario7.as_view()),
    path('scenario8/', Scenario8.as_view()),
    path('scenario9/', Scenario9.as_view()),
    path('scenario10/', Scenario10.as_view()),
    path('scenario11/', Scenario11.as_view()),
    path('scenario11/myobjects', Scenario11_1.as_view()),
    path('scenario11/myobjects/<int:id>/', Scenario11_2.as_view()),
    re_path(r'^scenario12/myobjects/(?P<id>\d+)/(?P<data>\D+)/', Scenario11_2.as_view()),
    re_path(r'^scenario12/myobjects/(?P<id>\d+)/', Scenario11_2.as_view()),

]
