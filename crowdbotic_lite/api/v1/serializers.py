from rest_framework import serializers
from crowdbotic_lite.models import GenerateModels


class GenerateModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateModels
        fields = "__all__"
