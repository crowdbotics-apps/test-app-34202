from rest_framework import authentication
from subscription_plan.models import SubscriptionPlans
from .serializers import SubscriptionPlansSerializer
from rest_framework import viewsets


class SubscriptionPlansViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionPlansSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SubscriptionPlans.objects.all()
