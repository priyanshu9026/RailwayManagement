from django.urls import path
from . import views

urlpatterns = [
    path('trains/', views.list_trains, name='list_trains'),
    path('trains/<int:train_id>/availability/', views.check_availability, name='check_availability'),
    path('trains/<int:train_id>/book/', views.book_seat, name='book_seat'),
]
