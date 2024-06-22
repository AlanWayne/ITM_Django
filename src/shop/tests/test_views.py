from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product


class TestViews(TestCase):
    
    def setUp(self):

        self.client = Client()

        self.product_1 = Product.objects.create(
            name="product_1",
        )

        self.detail_url = reverse(
            "product-detail",
            args=[self.product_1.id],
        )

        self.list_url = reverse(
            "product-list",
        )

    def test_product_list_get(self):

        response = self.client.get(
            self.list_url,
        )

        self.assertEquals(
            response.status_code,
            200,
        )

    def test_product_post(self):

        response = self.client.post(
            self.list_url,
            {
                "name": "product_2",
            },
        )

        self.assertEquals(
            response.status_code,
            201,
        )

        self.assertEquals(
            Product.objects.filter(name="product_2").count(),
            1,
        )

    def test_product_put(self):
        response = self.client.put(
            self.detail_url,
            data={
                "name": "product_1",
                "price": 1,
            },
            content_type="application/json",
        )

        self.assertEquals(
            response.status_code,
            200,
        )

    def test_product_delete(self):
        response = self.client.delete(
            self.detail_url,
            data={
                "name": "product_2",
            },
            content_type="application/json",
        )

        self.assertEquals(
            response.status_code,
            204,
        )

        self.assertEquals(
            Product.objects.filter(name="product_2").count(),
            0,
        )
