from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
