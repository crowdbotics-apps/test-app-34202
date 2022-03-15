from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SubscriptionPlansViewSet

router = DefaultRouter()
router.register("subscriptionplans", SubscriptionPlansViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
