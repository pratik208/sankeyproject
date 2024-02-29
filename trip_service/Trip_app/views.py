import genericpath
from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from warnings import filters
from django.shortcuts import render ,HttpResponse
from .models import Trip 
from Route_app.models import Route
from rest_framework.views import APIView
from Route_app.serializers import RouteSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django.http import JsonResponse

from .serializers import TripSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework import status
import requests
from django.http import JsonResponse
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.exceptions import ValidationError 
from rest_framework import status

class CustomPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size' 
    max_page_size = 500

class TripListAPIView(ListAPIView):
    queryset = Trip.objects.all()     # trip list all with the trip list view 
    serializer_class = TripSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['user_id' , 'trip_id']  
    search_fields = ['trip_id']
    


class TripDetailAPIView(APIView):
    def get(self, request, trip_id):
        try:
            trip = Trip.objects.get(trip_id=trip_id)
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data)  # Return JsonResponse instead of requests.Response
        except Trip.DoesNotExist:
            return JsonResponse({'error': 'Trip not found'}, status=404)
    
def index(request):
    return HttpResponse("Trip pages ...........")
@csrf_exempt
def create_trip(request):
    if request.method == 'POST':
        try:
            trip_data = JSONParser().parse(request)
            trip_serializer = TripSerializer(data=trip_data)
            if trip_serializer.is_valid():
                trip_serializer.save()
                return HttpResponse("Trip created successfully", status=status.HTTP_200_OK)
            else:
                return JsonResponse(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except ParseError:
            return JsonResponse({'message': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Only POST method is allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@csrf_exempt
def gettripid(request):
    if request.method == 'POST':
        try:
            trip_data = JSONParser().parse(request)
            print("hello")
           # trip_serializer = TripSerializer(data=trip_data)
           # if trip_serializer.is_valid():
              #  trip_serializer.save()
            #if trip_serializer.trip_id
            
            route_data=Route.objects.filter(route_origin=trip_data["route_origin"] , route_destination=trip_data["route_destination"]) 

            tripdata=Trip.objects.filter(route_id=route_data[0].route_id)
            print(tripdata[0])
            if tripdata[0].trip_id:
                responsedata={
                    "trip_id" : tripdata[0].trip_id
                }
                return JsonResponse(responsedata,status=status.HTTP_200_OK)           
            else:
                return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Only POST method is allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)