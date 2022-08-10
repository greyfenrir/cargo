import json
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from ..models import Shipment


class APITest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'admin@mail', 'a')
        self.user = User.objects.create_user('user', 'user@mail', 'u')
        Shipment.objects.create(from_addr='village1', to_addr='city1', owner=self.user)
        Shipment.objects.create(from_addr='village2', to_addr='city2', owner=self.admin)
        Shipment.objects.create(from_addr='village3', to_addr='city3', owner=self.user)

    def test_get_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        content = json.loads(response.content)
        admin_shipments = 0
        user_shipments = 0
        for record in content:
            if record['username'] == self.admin.username:
                admin_shipments += len(record['shipments'])
            elif record['username'] == self.user.username:
                user_shipments += len(record['shipments'])
            else:
                self.fail(f'Wrong owner found: {record["owner"]}')

        self.assertEqual(1, admin_shipments)
        self.assertEqual(2, user_shipments)

    def test_get_user_details(self):
        admin_id = 1
        url = reverse('user-details', args=[admin_id])
        response = self.client.get(url, format='json')
        content = json.loads(response.content)
        target_content = {'id': admin_id, 'username': 'admin', 'shipments': [2]}
        self.assertEqual(content, target_content)

    def test_get_shipment_list(self):
        url = reverse('shipment-list')
        response = self.client.get(url, format='json')
        content = json.loads(response.content)
        admin_shipments = 0
        user_shipments = 0
        for record in content:
            if record['owner'] == self.admin.username:
                admin_shipments += 1
            elif record['owner'] == self.user.username:
                user_shipments += 1
            else:
                self.fail(f'Wrong owner found: {record["owner"]}')

        self.assertEqual(1, admin_shipments)
        self.assertEqual(2, user_shipments)

    def test_add_shipment(self):
        url = reverse('shipment-list')
        response = self.client.post(url, format='json', data={'from_addr': 'village4', 'to_addr': 'city4', 'owner': 12})
        self.assertGreaterEqual(response.status_code, 400)  # anonymous user - access denied

        self.client.login(username=self.user.username, password='u')
        response = self.client.post(
            url, format='json', data={'from_addr': 'village4', 'to_addr': 'city4', 'owner': self.user.id})
        self.assertEqual(4, len(Shipment.objects.all()))

    def test_get_and_update_shipment_details(self):
        shipment_id = 1
        old_state = Shipment.STATES[0][0]
        new_state = Shipment.STATES[1][0]
        url = reverse('shipment-details', args=[shipment_id])
        response = self.client.get(url, format='json')
        content = json.loads(response.content)
        self.assertEqual(old_state, content['state'])

        content['state'] = new_state

        # anonymous user - access denied
        response = self.client.put(url, content)
        self.assertGreaterEqual(response.status_code, 400)

        # wrong user - access denied
        self.client.login(username=self.admin.username, password='a')
        response = self.client.put(url, content)
        self.assertGreaterEqual(response.status_code, 400)

        self.client.login(username=self.user.username, password='u')
        response = self.client.put(url, content)
        self.assertLess(response.status_code, 300)
        self.assertEqual(new_state, Shipment.objects.all()[0].state)

    def test_delete_shipment(self):
        shipment_id = 1
        url = reverse('shipment-details', args=[shipment_id])
        self.client.login(username=self.user.username, password='u')
        response = self.client.delete(url)
        self.assertLess(response.status_code, 300)
        self.assertEqual(2, len(Shipment.objects.all()))



