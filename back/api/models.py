from django.db import models

# Create your models here.
from django.db import models


class Shipment(models.Model):
    STATES = (
        ('Receiving', 'Receiving'),
        ('Processing', 'Processing'),
        ('Fulfilling', 'Fulfilling'),
        ('Done', 'Done')

    )
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.TextField(default='')
    to_addr = models.TextField(default='')

    state = models.CharField(max_length=10, choices=STATES, default=STATES[0][0])

    owner = models.ForeignKey('auth.User', related_name='shipments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
