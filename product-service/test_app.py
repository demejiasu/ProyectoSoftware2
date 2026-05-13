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

    def test_2_create_product_returns_201(self):
        """Test POST /products creates a product and returns 201"""
        response = self.app.post(
            '/products',
            data=json.dumps({'name': 'Test Product', 'price': 10.99, 'stock': 5}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('_id', data)

    def test_3_update_product_not_found_returns_404(self):
        """Test PUT /products/:id returns 404 for non-existent id"""
        response = self.app.put(
            '/products/507f1f77bcf86cd799439011',
            data=json.dumps({'name': 'Updated'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_4_delete_product_not_found_returns_404(self):
        """Test DELETE /products/:id returns 404 for non-existent id"""
        response = self.app.delete('/products/507f1f77bcf86cd799439011')
        self.assertEqual(response.status_code, 404)

    def test_5_create_product_without_name_returns_400(self):
        """Test POST /products without name returns 400"""
        response = self.app.post(
            '/products',
            data=json.dumps({'price': 10.99}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()