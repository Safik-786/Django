from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by("name")