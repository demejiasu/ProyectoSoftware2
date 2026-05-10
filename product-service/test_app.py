import unittest
import json
from app import app

class ProductServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_1_list_products_returns_json(self):
        """Test GET /products returns a list"""
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_2_create_product_returns_id(self):
        """Test POST /products creates a product"""
        response = self.app.post(
            '/products',
            data=json.dumps({'name': 'Test Product', 'price': 10.99, 'stock': 5}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)

    def test_3_update_product_returns_success(self):
        """Test PUT /products/:id updates a product"""
        response = self.app.put(
            '/products/507f1f77bcf86cd799439011',
            data=json.dumps({'name': 'Updated'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_4_delete_product_returns_success(self):
        """Test DELETE /products/:id deletes a product"""
        response = self.app.delete('/products/507f1f77bcf86cd799439011')
        self.assertEqual(response.status_code, 200)

    def test_5_create_product_missing_price_fails(self):
        """Test POST /products without price returns error"""
        response = self.app.post(
            '/products',
            data=json.dumps({'name': 'No Price'}),
            content_type='application/json'
        )
        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()