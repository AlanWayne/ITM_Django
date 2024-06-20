from django.db.models import Model, ForeignKey, CASCADE
from django.db.models import DateTimeField, ImageField
from django.db.models import DecimalField, PositiveIntegerField
from django.db.models import TextField, CharField
from django.forms import ChoiceField, RadioSelect
from django.contrib.auth.models import User


class Product(Model):

    name = CharField(
        max_length=255,
        unique=True,
    )

    description = TextField(
        blank=True,
    )

    price = DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
    )

    manufacturer = CharField(
        blank=True,
        max_length=255,
    )

    model = CharField(
        blank=True,
        max_length=255,
    )

    image_url = ImageField(
        blank=True,
        upload_to="img",
    )

    def __str__(self) -> str:

        return self.name


class Cart(Model):

    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )

    product = ForeignKey(
        Product,
        on_delete=CASCADE,
    )

    quantity = PositiveIntegerField(
        default=1,
    )

    class Meta:

        unique_together = (
            "user",
            "product",
        )

    def __str__(self) -> str:

        return f"{self.user.username} :: {self.product.name}"


class Order(Model):

    STATUS_CHOICES = (
        ("created", "CREATED"),
        ("in_process", "IN PROCESS"),
        ("ready", "READY"),
        ("done", "DONE"),
        ("cancelled", "CALCELLED"),
    )

    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )

    order_date = DateTimeField(
        auto_now_add=True,
    )

    total_price = DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
    )

    status = ChoiceField(
        choices=STATUS_CHOICES,
        widget=RadioSelect,
    )

    def __str__(self) -> str:

        return f"No. {self.id} by {self.user.username}"


class OrderProduct(Model):

    order = ForeignKey(
        Order,
        on_delete=CASCADE,
    )

    product = ForeignKey(
        Product,
        on_delete=CASCADE,
    )

    quantity = PositiveIntegerField(
        default=1,
    )

    def __str__(self) -> str:

        return f"{self.product.name} :: {self.order}"


class Review(Model):

    RATING_CHOICES = {
        "1": "Very bad",
        "2": "Bad",
        "3": "Normal",
        "4": "Good",
        "5": "Very good",
    }

    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )
    
    product = ForeignKey(
        Product,
        on_delete=CASCADE,
    )
    
    rating = CharField(
        choices=RATING_CHOICES,
        default="5",
    )
    
    comment = TextField(
        blank=True,
    )

    def __str__(self) -> str:
        
        return f"{self.user.username} :: {self.product.name}"
