from django.contrib import admin
from .models import Product, Cart, Order, OrderProduct, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "manufacturer",
        "model",
        "image_url",
    )
    list_filter = ("price", "manufacturer")
    fieldsets = (
        (
            "Title",
            {
                "fields": ("name", ("model", "manufacturer")),
            },
        ),
        ("Description", {"fields": ("description", "price", "image_url")}),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user_id", "product_id", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user_id", "order_date", "total_price", "status")


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("order_id", "product_id", "quantity")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user_id", "product_id", "rating", "comment")
