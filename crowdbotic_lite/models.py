from django.conf import settings
from django.db import models


class GenerateModels(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        null=True,
        blank=True,
    )
    date_modified = models.DateTimeField(
        null=True,
        blank=True,
    )
    user_created = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="generatemodels_user_created",
    )


# Create your models here.
