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
    booking_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    start_date = models.TimeField(unique='DD-MM-YYYY')
    end_date = models.TimeField(unique='DD-MM-YYYY')
    total_price = models.DecimalField()
    status = models.enums('pending', 'confirmed', 'canceled')
    created_at = models.TimeField(auto_now=True)

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL)
    rating = models.IntegerChoices(1,2,3,4,5)
    comment = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
