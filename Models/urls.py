from django.urls import path, include
from django.conf.urls import url
from .views import  Scenario1, Scenario2, Scenario3
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

# router.register('scenario1', Scenario1)
#
#
# urlpatterns = [
#     path('',include(router.urls)),
# ]

urlpatterns = [
    path('scenario1/',Scenario1.as_view()),
    path('scenario2/',Scenario2.as_view()),
    path('scenario3/',Scenario3.as_view()),
]