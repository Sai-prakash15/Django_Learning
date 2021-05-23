from rest_framework import viewsets, permissions
from .models import Articler, Reporter
from rest_framework.views import APIView
from .serializers import ArticlerSerializer
from django.db import connection
from rest_framework.response import Response

from django.db.models import Count, F, Value
import json
# Create your views here.

## tried to implement with generics and model viewsets same behaviour
# class Scenario1(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # queryset = Articler.objects.all()
#     serializer_class = Scenario1Serializer
#     lookup_field = 'id'
#     search_fields = ["headline"]
#
#     def get_queryset(self):
#         qs = Articler.objects.all()
#
#         #Custom filtering
#         query1 = self.request.GET.get('id')
#         query2 = self.request.GET.get('headline')
#         if  query1 is not None and query2 is not None:
#             qs = qs.filter(id=query1).filter(headline__iendswith=query2)
#         elif query1 is not None:
#             qs = qs.filter(id=query1)
#         elif query2 is not None:
#             qs = qs.filter(headline__iendswith=query2)
#
#         #printing foreign key field data
#
#         # for i in qs:
#         #     #print(qs)
#         #     # print(i.reporter.first_name)
#         #     print(i.reporter.first_name)
#         # print(self.request.user)
#         print(len(connection.queries))
#         return qs

## Using API view
class Scenario1(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):


        qs = Articler.objects.all()

        # Custom filtering
        query1 = self.request.GET.get('id')
        query2 = self.request.GET.get('headline')
        if query1 is not None and query2 is not None:
            qs = qs.filter(id=query1).filter(headline__iendswith=query2)
        elif query1 is not None:
            qs = qs.filter(id=query1)
        elif query2 is not None:
            qs = qs.filter(headline__iendswith=query2)

        ## printing foreign key field data
        # Iterating
        # for i in qs:
        #     #print(qs)
        #     # print(i.reporter.first_name)
        #     print(i.reporter.firstname)
        # print(self.request.user)

        #using queries
        temp = Articler.objects.values("reporter__firstname")
        print(temp)

        queries = len(connection.queries)
        temp = {}
        temp["queries"] = queries
        serialized_data = ArticlerSerializer(qs, many=True)
        data = [temp]
        return Response(serialized_data.data + data)

    # def post(self, request, format=None):
    #     qs = ToDoList.objects.all()
    #     print(qs)
    #     serialized_data = ToDoListSerializer(qs, many=True)
    #     return Response(serialized_data.data)

class Scenario2(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):


        qs = Articler.objects.values_list(F("id")+100, flat=True)

        return Response(qs)

class Scenario3(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        qs = Reporter.objects.all()
        temp = []
        for i in qs:
            temp.append({"id": i.id,"count_of_related_objects":i.articler_set.count()})
        return Response(temp)


from faker import Faker
from .models import Place
from .serializers import PlaceSerializer
from rest_framework import status
from itertools import islice
class Scenario4(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def post(self, request, format=None):
        print("here")
        fake = Faker()
        data = []
        objs = (Place(name=fake.name(),address= fake.address()) for i in range(100000))
        print(objs)
        batch_size = 10000

        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Place.objects.bulk_create(batch, batch_size)
            print("in process...")

        return Response(status=status.HTTP_201_CREATED)


#Not yet implemented
class Scenario5(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def post(self, request, format=None):
        # serializer = PlaceSerializer(data=request.data)
        print(request.data)


        return Response(status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)