from rest_framework import viewsets, permissions
from .models import Articler, Reporter
from rest_framework.views import APIView
from .serializers import ArticlerSerializer, InformationXSerializer
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

        # using queries
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
        qs = Articler.objects.values_list(F("id") + 100, flat=True)

        return Response(qs)


class Scenario3(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        qs = Reporter.objects.all()
        temp = []
        for i in qs:
            temp.append({"id": i.id, "count_of_related_objects": i.articler_set.count()})
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
        objs = (Place(name=fake.name(), address=fake.address()) for i in range(100000))
        print(objs)
        batch_size = 10000

        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                print("Finally")
                break
            Place.objects.bulk_create(batch, batch_size)
            print("in process...")

        return Response(status=status.HTTP_201_CREATED)


import datetime


class Scenario5(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        # serializer = PlaceSerializer(data=request.data)
        search_list = request.data
        start_time = datetime.datetime.now()
        print("started")
        # res  = Place.objects.in_bulk(search_list, field_name='name') #name field must be unique
        res = 0
        for i in search_list:
            res += Place.objects.filter(name__contains=i).count()
        end_time = datetime.datetime.now()
        print(f"Looked up in {end_time - start_time}")

        return Response(res, status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Person
# from .serializers import PersonSerializer

class Scenario6(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        qs = Person.objects.all()

        # Custom filtering
        res = []
        for i in qs:
            res.append({"id": i.id, "vehicles": i.vehiclexx_set.values("lp_number"),
                        "Information": InformationXSerializer(i.information.all(), many=True).data, "task": i.task.taskName, "place": i.place.name})
        print(res)
        return Response(res + [ {"queries" : len(connection.queries)}])
from django.core import serializers
from django.http import JsonResponse
class Scenario7(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):

        res =  Person.objects.values("id","information__content", "task__taskName","place__name")
        res = list(res)
        res.append({"queries" : str(len(connection.queries))})
        # # print(res)
        # # print(json.dumps(list(res)))
        # json_res = json.dumps(list(res))
        # print(json_res)
        # res_list = serializers.serialize("json", list(res), fields=('information__content','task__taskName', "place__name")) # Not working
        return Response(res)

from .serializers import PersonSerializer
class Scenario8(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        temp = []
        res =  Person.objects.values("id")
        temp.append({"values": list(res)})

        res = Person.objects.values_list("id")
        temp.append({"values_List": list(res)})

        res = PersonSerializer(Person.objects.only("id"), many=True).data
        temp.append({"only": res})

        res = PersonSerializer(Person.objects.defer("information", "place","task","name"), many=True).data
        temp.append({"defer": res})


        temp.append({"queries": str(len(connection.queries))})

        return Response(temp)


class Scenario9(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        data = request.data
        print(data)
        for i in data:
            if "id" in i and Place.objects.filter(id=i.get("id")).exists():
                p = Place.objects.get(id=i.get("id"))
                p.name = i.get("name")
                p.save()
            else:
                p = Place(name=i.get("name"))
                print(p)
                p.save()

        return Response(data, status=status.HTTP_201_CREATED)

from .models import Temp
class Scenario10(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        data = request.data # input list of id's
        # print(data)
        l = len(data)
        res = []
        for i in range(l//2):
            # print("i",data[i],i)
            if  Temp.objects.filter(id=data[i]).exists():
                with connection.cursor() as cursor:
                    cursor.execute('DELETE FROM "Models_temp" WHERE id = %s', [data[i]])
                res.append(data[i])
        for j in range(l//2, l):
            if Temp.objects.filter(id=data[j]).exists():
                res.append(data[j])
                Temp.objects.get(id=data[j]).delete()

        return Response([{"deleted ids": res}], status=status.HTTP_201_CREATED)

class Scenario11(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        temp = []
        res =  Person.objects.values("id")
        temp.append({"values": list(res)})

        res = Person.objects.values_list("id")
        temp.append({"values_List": list(res)})

        res = PersonSerializer(Person.objects.only("id"), many=True).data
        temp.append({"only": res})

        res = PersonSerializer(Person.objects.defer("information", "place","task","name"), many=True).data
        temp.append({"defer": res})


        temp.append({"queries": str(len(connection.queries))})

        return Response(temp)

class Scenario11_1(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        temp = []
        temp.append({"count": str(Person.objects.count())})

        return Response(temp)

def is_json(data):
    try:
        json_data = json.loads(data)
        is_valid = True
    except:
        is_valid = False
    return is_valid
from .serializers import PersonSerializerX
class Scenario11_2(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request,id, format=None):
        data = request.GET.get('data', None)
        if(Person.objects.filter(id=id).exists()):
            if(data == "true"):
                return Response(PersonSerializerX(Person.objects.get(id=id)).data)
            else:
                return Response("False")
        else:
            return Response("False")