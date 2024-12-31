from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
class Listing(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    host_id = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    location = models.CharField(max_length=30)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now_add=True)

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]


    booking_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    start_date = models.TimeField(unique='DD-MM-YYYY')
    end_date = models.TimeField(unique='DD-MM-YYYY')
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    created_at = models.TimeField(auto_now=True)

class Review(models.Model):
    class Ratings(models.IntegerChoices):
        ONE = 1, '1 - Poor'
        TWO = 2, '2 - Fair'
        THREE = 3, '3 - Good'
        FOUR = 4, '4 - Very Good'
        FIVE = 5, '5 - Excellent'
    review_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(
        choices=Ratings.choices,
        default=Ratings.THREE,  # Default to "3 - Good"
    )
    comment = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
