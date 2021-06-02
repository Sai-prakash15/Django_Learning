from rest_framework import serializers

from .models import (
    AuthToken,
)



class AuthTokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = "__all__"

    def create(self, validated_data):
        authtoken = AuthToken(**validated_data)
        authtoken.save()
        return authtoken