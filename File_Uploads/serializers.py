from rest_framework import serializers

class GeeksSerializer(serializers.Serializer):
    # intialize fields
    files = serializers.FileField()