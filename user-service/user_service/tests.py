from django.test import TestCase, Client
from django.urls import reverse
import json

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_user = {
            'name': 'Test User',
            'email': 'test@test.com',
            'password': 'test123',
            'role': 'user',
            'status': 'active'
        }

    def test_1_list_users_returns_json(self):
        """Test GET /users returns a list"""
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('users', data)

    def test_2_create_user_returns_201(self):
        """Test POST /users creates a user and returns 201"""
        response = self.client.post(
            '/users',
            data=json.dumps(self.valid_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertIsNotNone(data.get('id'))

    def test_3_update_user_returns_success(self):
        """Test PUT /users/:id updates a user"""
        response = self.client.put(
            '/users/1',
            data=json.dumps({'name': 'Updated Name'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_4_delete_user_returns_success(self):
        """Test DELETE /users/:id deletes a user"""
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_5_create_user_without_email_creates_with_default(self):
        """Test POST /users creates user even without optional fields"""
        response = self.client.post(
            '/users',
            data=json.dumps({'name': 'Test User'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
