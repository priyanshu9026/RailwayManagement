from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_trains(request):
    # Example response
    trains = [
        {'id': 1, 'train_number': '12345', 'start_station': 'Station A', 'end_station': 'Station B'},
        {'id': 2, 'train_number': '67890', 'start_station': 'Station C', 'end_station': 'Station D'},
    ]
    return Response(trains)
