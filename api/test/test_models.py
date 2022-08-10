
from django.test import TestCase
from ..models import Shipment


class ShipmentTest(TestCase):
    def setUp(self):
        Shipment.objects.create(from_addr='village', to_addr='city')

    def test_empty(self):
        pass

