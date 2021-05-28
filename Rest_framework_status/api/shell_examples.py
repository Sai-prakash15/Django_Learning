from Rest_framework_status.models import Status
from Rest_framework_status.api.serializers import StatusSerializer

##JSON

# serializing the data


# deserializing the data


## Validating data

# Creating obj
data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()

# if serializer.is_valid(): # form.is_valid()
#     serializer.save()

# Updating obj
obj = Status.objects.first()
data = {'content': 'some new content', "user": 1}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()

# Delete obj # Serilizer is not used to delte but we can create objects with serializers, update objects with them

data = {'user': 1, "content": "please delete me"}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

data = {'id': 5}
obj = Status.objects.last()
# get_data_serializer = StatusSerializer(obj, data=data)
# update_serializer.is_valid()
print(obj.delete())

from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    email = serializers.EmailField()


create_obj_serializer = CustomSerializer(data=data)

if create_obj_serializer.is_valid():  # form.is_valid()
    valid_data = create_obj_serializer.data
    print(valid_data)
