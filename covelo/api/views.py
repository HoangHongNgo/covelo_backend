from rest_framework import generics
from .serializers import BicycleSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bicycle, Station, Locker
from .serializers import CustomUserSerializer, LockerSerializer, StationSerializer, BicycleSerializer


@csrf_exempt
@api_view(['POST'])
def register(request):
    """
    Register new user.
    """
    if request.method == 'POST':
        # Parse data from request's body into a serializer
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user with the provided data
            user = serializer.save()

            # Send a response to the client
            response_data = {
                'user_id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'type': user.type
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        # If serializer is invalid, send error message to client
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def userlogin(request):
    """
    Login user.
    """
    if request.method == 'POST':
        # Get username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user with the provided username and password
        user = authenticate(
            request=request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request=request, user=user)

            # Send a response to the client
            response_data = {
                'user_id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'type': user.type
            }
            return Response(response_data, status=status.HTTP_200_OK)

        # If authentication fails, send error message to client
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_bicycle(request):
    """
    Create a new Bicycle instance.
    """
    if request.method == 'POST':
        serializer = BicycleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_station(request):
    """
    Create a new Station instance.
    """
    if request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_locker(request):
    """
    Create a new Locker instance.
    """
    if request.method == 'POST':
        serializer = LockerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def locker_detail(request, locker_id):
    try:
        locker = Locker.objects.get(locker_id=locker_id)
        serializer = LockerSerializer(locker)
        return Response(serializer.data)
    except Locker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class BicycleDetailView(generics.RetrieveAPIView):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer


@api_view(['POST'])
def Unlock_Bicycle(request):
    try:
        bicycle_id = request.data.get('bicycle_id')
        bicycle = Bicycle.objects.get(bicycle_id=bicycle_id)
        locker = bicycle.locker
        if locker:
            locker.is_locked = False
            locker.save()
            bicycle.locker = None
            bicycle.save()
            return Response({"message": "Bicycle unlocked successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "This bicycle is not locked."}, status=status.HTTP_400_BAD_REQUEST)
    except Bicycle.DoesNotExist:
        return Response({"message": "This bicycle does not exist."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def Lock_Bicycle(request):
    try:
        bicycle_id = request.data.get('bicycle_id')
        bicycle = Bicycle.objects.get(bicycle_id=bicycle_id)
        locker_id = request.data.get('locker_id')
        locker = Locker.objects.get(locker_id=locker_id)
        if not bicycle.locker:
            locker.is_locked = True
            locker.save
            bicycle.locker = locker
            bicycle.save()
            return Response({"message": "Locked successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "This bicycle is already locked."}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"message": "Locker or Bicycle does not exist"}, status=status.HTTP_404_NOT_FOUND)
