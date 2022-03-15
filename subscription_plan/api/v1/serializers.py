from rest_framework import serializers
from subscription_plan.models import SubscriptionPlans


class SubscriptionPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlans
        fields = "__all__"
