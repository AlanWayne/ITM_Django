from django.forms import Form, DecimalField, Textarea, RadioSelect
from .models import Review


class ProductFilter(Form):
    max_price = DecimalField(label="max-price")
    min_price = DecimalField(label="min-price")


class ReviewForm(Form):

    class Meta:

        RATING_CHOICES = {
            "1": "Very bad",
            "2": "Bad",
            "3": "Normal",
            "4": "Good",
            "5": "Very good",
        }

        model = Review
        fields = ["user_id", "product_id", "rating", "comment"]
        widgets = {"rating": RadioSelect(choices=RATING_CHOICES), "comment": Textarea}
