from rest_framework import viewsets, mixins, permissions, pagination
from rest_framework.authentication import SessionAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response

from Rest_framework_status.models import Status
from .serializers import StatusSerializer


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format= None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format = None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


# class StatusAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format= None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format = None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)




class StatusAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'
    search_fields = ["user__username", "content"]

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     print(self.request.user)
    #     return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
