from rest_framework import serializers

from Models.models import Articler



class Scenario1Serializer(serializers.ModelSerializer):
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