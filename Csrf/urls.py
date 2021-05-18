from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    # path('<int:id>/', Status_detail),
    # url('create/$', StatusAPIView.as_view()),
    # url(r'^(?P<id>.*)/$',StatusAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$',StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$',StatusDeleteAPIView.as_view()),
]