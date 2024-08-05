from django.contrib import admin
from .models import CustomUser, Train, Booking

admin.site.register(CustomUser)
admin.site.register(Train)
admin.site.register(Booking)
