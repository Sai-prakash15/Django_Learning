from rest_framework import serializers

from Models.models import Articler, Place, InformationX, Person



class ArticlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articler
        fields = [
            'id',
            'headline',
            'pub_date',
            'reporter'
        ]
        read_only_fields = ['user']
    # def validate_content(self, value):
    #     if len(value) > 10000000:
    #         raise serializers.ValidationError("Way too long")
    #     return value

    def validate(self, data):
        headline = data.get("headline", None)
        if headline == "":
            headline = None
        if headline is None :
            raise serializers.ValidationError("headline is required")
        return data


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'address',
        ]
        read_only_fields = ['user']
    # def validate_content(self, value):
    #     if len(value) > 10000000:
    #         raise serializers.ValidationError("Way too long")
    #     return value

    def validate(self, data):
        name = data.get("name", None)
        if name == "":
            headline = None
        if name is None :
            raise serializers.ValidationError("name is required")
        return data

class InformationXSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationX
        fields = [
            'id',
            'content',
        ]
        read_only_fields = ['user']
    # def validate_content(self, value):
    #     if len(value) > 10000000:
    #         raise serializers.ValidationError("Way too long")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        if content is None :
            raise serializers.ValidationError("content is required")
        return data

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'information',
            'place',
            'task'
        ]
        read_only_fields = ['user']
    # def validate_content(self, value):
    #     if len(value) > 10000000:
    #         raise serializers.ValidationError("Way too long")
    #     return value

    # def validate(self, data):
    #     content = data.get("content", None)
    #     if content == "":
    #         content = None
    #     if content is None :
    #         raise serializers.ValidationError("content is required")
    #     return data