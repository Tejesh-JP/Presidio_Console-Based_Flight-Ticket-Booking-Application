from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    flight_name = models.CharField(max_length=255)
    date = models.DateField()
    seat_count = models.IntegerField(default=60)
    booked_seats = models.IntegerField(default=0)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)