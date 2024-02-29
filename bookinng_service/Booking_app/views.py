import genericpath
from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from django.shortcuts import render ,HttpResponse
import requests
from rest_framework.views import APIView
from .serializers import BookingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Booking
from .serializers import BookingSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class BookingListAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
 #   ordering_fields = ['ticket_id']

class BookingDetailAPIView(APIView):
    def get_object(self, ticket_id):
        try:
            return Booking.objects.get(ticket_id=ticket_id)
        except Booking.DoesNotExist:
            raise Http404("Booking not found")

    def get(self, request, ticket_id, format=None):
        try:
            booking = self.get_object(ticket_id)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404 as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def index(request):
    return HttpResponse("Homeeeeeeeeee page")

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            booking_data = JSONParser().parse(request)
            
            
           
            booking_url = 'http://127.0.0.1:8001/trip_app/gettrip_id'
        
            booking_response = requests.post(booking_url, json={'route_origin':booking_data["route_origin"] , 'route_destination':booking_data["route_destination"]})
            print(booking_response)
            if booking_response.status_code == 200:
                print(booking_response.json()["trip_id"])
               # booking_responsedata=booking_response.json()
                #print(booking_responsedata)
                bookingdata={'ticket_id':booking_data["ticket_id"] , 'trip_id':booking_response.json()["trip_id"] ,'traveler_name':booking_data["traveler_name"] ,'traveler_number':booking_data["traveler_number"],'ticket_cost':booking_data["ticket_cost"],'traveler_email':booking_data["traveler_email"]}
                booking_serializer = BookingSerializer(data=bookingdata)
                if booking_serializer.is_valid():
                    
                    booking_serializer.save()
                    return JsonResponse({'message': ' trip  Booking created successfully'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(booking_serializer.errors, status=400)
            else:
                return JsonResponse({'message': 'Failed to create trip booking'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
           
        except (JSONDecodeError, ParseError):
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Only POST method is allowed", status=405)