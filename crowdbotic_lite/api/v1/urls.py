from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GenerateModelsViewSet

router = DefaultRouter()
router.register("generatemodels", GenerateModelsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
