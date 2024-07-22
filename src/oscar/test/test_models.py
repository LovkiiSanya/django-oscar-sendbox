from django.test import TestCase
from oscar.test.factories import ProductFactory, ProductClassFactory
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')

class ProductTestCase(TestCase):
    def setUp(self):
        self.product_class = ProductClassFactory(name="Default")
        self.product = ProductFactory(product_class=self.product_class)

    def test_create_product_with_test_field(self):
        # Test creating a product with test_field
        product = Product.objects.create(
            title='Test Product',
            upc='123456789012',
            product_class=self.product_class,
            test_field='Test Field Value'
        )
        self.assertEqual(product.test_field, 'Test Field Value')

    def test_update_product_test_field(self):
        # Test updating the test_field of a product
        self.product.test_field = 'Updated Test Field Value'
        self.product.save()
        self.assertEqual(self.product.test_field, 'Updated Test Field Value')

    def test_search_product_by_test_field(self):
        # Test searching a product by test_field
        Product.objects.create(
            title='Another Product',
            upc='987654321098',
            product_class=self.product_class,
            test_field='Searchable Value'
        )
        products = Product.objects.filter(test_field='Searchable Value')
        self.assertEqual(products.count(), 1)
        self.assertEqual(products[0].test_field, 'Searchable Value')
