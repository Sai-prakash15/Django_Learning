from django.urls import path, include
from django.conf.urls import url
from .views import StatusAPIView
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

router.register('', StatusAPIView)

# Status_API_View = StatusAPIView.as_view(
#     {
#         'get': 'list',
#         'post': 'create'
#     }
# )
#
# Status_detail = StatusAPIView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:id>/', Status_detail),
    # url('create/$', StatusAPIView.as_view()),
    # url(r'^(?P<id>.*)/$',StatusAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$',StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$',StatusDeleteAPIView.as_view()),
]

# /api/status/ -> list
# /api/status/create -> create
# /api/status/12/ -> detail
# /api/status/12/update -> Update
# /api/status/12/delete -> delete


# /api/status/ -> List -> CRUD
# /api/status/12/ -> detail -> CRUD


# /api/status/ -> crud & ls
