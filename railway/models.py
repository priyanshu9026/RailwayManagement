from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Train(models.Model):
    train_number = models.CharField(max_length=10)from django.db import models
from django.contrib.auth.models import User

class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    start_station = models.ForeignKey(Station, related_name='start_station', on_delete=models.CASCADE)
    end_station = models.ForeignKey(Station, related_name='end_station', on_delete=models.CASCADE)
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.train_number} - {self.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    start_station = models.CharField(max_length=100)
    end_station = models.CharField(max_length=100)
    total_seats = models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booking_status = models.BooleanField(default=False)
