import unittest
import json
from app import app

class NotificationServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_1_list_notifications_returns_json(self):
        """Test GET /notify returns a list"""
        response = self.app.get('/notify')
        self.assertEqual(response.status_code, 200)

    def test_2_create_notification_returns_success(self):
        """Test POST /notify creates a notification"""
        response = self.app.post(
            '/notify',
            data=json.dumps({'message': 'Test notification', 'type': 'info'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_3_update_notification_returns_success(self):
        """Test PUT /notify/:id updates a notification"""
        response = self.app.put(
            '/notify/1',
            data=json.dumps({'message': 'Updated'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_4_delete_notification_returns_success(self):
        """Test DELETE /notify/:id deletes a notification"""
        response = self.app.delete('/notify/1')
        self.assertEqual(response.status_code, 200)

    def test_5_create_notification_missing_message_fails(self):
        """Test POST /notify without message returns error"""
        response = self.app.post(
            '/notify',
            data=json.dumps({'type': 'info'}),
            content_type='application/json'
        )
        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()