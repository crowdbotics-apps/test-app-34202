from django.conf import settings
from django.db import models


class SubscriptionPlans(models.Model):
    "Generated Model"
    tier = models.TextField(
        max_length=50,
        blank=True,
    )
    price = models.IntegerField(
        blank=True,
    )
    date_created = models.DateTimeField(
        blank=True,
    )
    date_updated = models.DateTimeField(
        blank=True,
    )
    crowdbotic_lite = models.ForeignKey(
        "crowdbotic_lite.GenerateModels",
        on_delete=models.CASCADE,
        blank=True,
        related_name="subscriptionplans_crowdbotic_lite",
    )


# Create your models here.
