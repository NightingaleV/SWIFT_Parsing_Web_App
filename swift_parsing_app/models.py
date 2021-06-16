import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    full_name = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=86, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(_('creation date and time'), auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(_('modification date and time'), auto_now=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'customer'

    def get_absolute_url(self):
        return reverse('swift_parsing:customer-detail', kwargs={'customer_id': self.id})

    def __str__(self):
        return f"{self.full_name}"
