from django.conf import settings
from django.db import models


class Subscriptions(models.Model):
    "Generated Model"
    crowdbotic_lite = models.ForeignKey(
        "crowdbotic_lite.GenerateModels",
        on_delete=models.CASCADE,
        related_name="subscriptions_crowdbotic_lite",
    )
    is_active = models.BooleanField()
    start_date = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )
    users = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscriptions_users",
    )
    plan = models.ForeignKey(
        "subscription_plan.SubscriptionPlans",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscriptions_plan",
    )


# Create your models here.
