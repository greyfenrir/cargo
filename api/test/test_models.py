
from django.contrib.auth.models import User

from django.test import TestCase
from ..models import Shipment


class ShipmentTest(TestCase):
    def test_empty(self):
        owner_a = User(username='admin')
        owner_u = User(username='user')
        owner_a.save()
        owner_u.save()
        Shipment.objects.create(from_addr='village1', to_addr='city1', owner=owner_u)
        Shipment.objects.create(from_addr='village2', to_addr='city2', owner=owner_a)
        Shipment.objects.create(from_addr='village3', to_addr='city3', owner=owner_u)
        admin_shipments = Shipment.objects.filter(owner=owner_a.id)
        user_shipments = Shipment.objects.filter(owner=owner_u.id)
        self.assertEqual(1, len(admin_shipments))
        self.assertEqual(2, len(user_shipments))
        self.assertTrue(admin_shipments[0].created)     # not empty
        self.assertTrue('Receiving', admin_shipments[0].state)  # default value


