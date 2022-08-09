from django.db import models

# Create your models here.
from django.db import models


class Shipment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.TextField(default='')
    to_addr = models.TextField(default='')

    # Receiving, Processing, Fulfilling
    state = models.TextField(default='Receiving')   # todo: convert to ChoiceField

    owner = models.ForeignKey('auth.User', related_name='shipments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
