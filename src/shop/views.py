from .models import *
from .serializers import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated


# API


class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]


class CartViewSet(viewsets.ModelViewSet):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user"]
    permission_classes = (IsAuthenticated,)


class OrderViewSet(viewsets.ModelViewSet):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id", "user", "order_date", "status"]
    permission_classes = (IsAuthenticated,)


class OrderProductViewSet(viewsets.ModelViewSet):
    
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["id", "order", "product"]
    permission_classes = (IsAuthenticated,)


class ReviewViewSet(viewsets.ModelViewSet):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user", "product", "rating"]
    permission_classes = (IsAuthenticated,)


# User


def review(request):
    
    return render(request, "shop/review.html")


def catalog(request):
    
    product = Product.objects.all()

    param_search = request.GET.get("search")
    if param_search:
        product = product.filter(name__icontains=param_search)

    param_min_price = request.GET.get("min-price")
    if param_min_price:
        product = product.filter(price__gte=param_min_price)

    param_max_price = request.GET.get("max-price")
    if param_max_price:
        product = product.filter(price__lte=param_max_price)

    max_price = product.aggregate(Max("price")).get("price__max")
    min_price = product.aggregate(Min("price")).get("price__min")

    return render(
        request,
        "shop/catalog.html",
        {"product": product, "max_price": max_price, "min_price": min_price},
    )


def about(request):
    
    return render(request, "shop/about.html")
