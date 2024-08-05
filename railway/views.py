from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Train, Booking
from .serializers import TrainSerializer, BookingSerializer
from django.db import transaction

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_trains(request):
    # Logic to fetch available trains between stations
    trains = Train.objects.all()
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_availability(request, train_id):
    # Logic to check seat availability
    try:
        train = Train.objects.get(id=train_id)
        available_seats = train.total_seats - Booking.objects.filter(train=train, booking_status=True).count()
        return Response({'available_seats': available_seats})
    except Train.DoesNotExist:
        return Response({'error': 'Train not found'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def book_seat(request, train_id):
    # Logic to book a seat with race condition handling
    try:
        train = Train.objects.get(id=train_id)
        available_seats = train.total_seats - Booking.objects.filter(train=train, booking_status=True).count()

        if available_seats > 0:
            # Create a new booking
            booking = Booking(user=request.user, train=train, seat_number=available_seats, booking_status=True)
            booking.save()
            return Response({'success': 'Booking successful'})
        else:
            return Response({'error': 'No seats available'}, status=400)
    except Train.DoesNotExist:
        return Response({'error': 'Train not found'}, status=404)
