from rest_framework import authentication
from crowdbotic_lite.models import GenerateModels
from .serializers import GenerateModelsSerializer
from rest_framework import viewsets


class GenerateModelsViewSet(viewsets.ModelViewSet):
    serializer_class = GenerateModelsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = GenerateModels.objects.all()
