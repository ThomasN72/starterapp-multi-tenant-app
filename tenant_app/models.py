from django.db import models
from django_multitenant.models import TenantModel


class Region(TenantModel):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    tenant_id = "id"

    def __str__(self):
        return self.name


class Member(TenantModel):
    name = models.CharField(max_length=100)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["id", "region"]

    class TenantMeta:
        tenant_field_name = "region_id"
