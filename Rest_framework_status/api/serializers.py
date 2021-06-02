from rest_framework import serializers

from Rest_framework_status.models import Status

'''
Serializer -> JSON
Serializer -> Validate data
'''


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
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
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required")
        return data
