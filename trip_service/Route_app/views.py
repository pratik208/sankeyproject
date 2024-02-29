from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from warnings import filters
from django.shortcuts import render ,HttpResponse
from requests import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter ,SearchFilter
from .models import Route
from rest_framework.views import APIView
from .serializers import RouteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework import status
# Create your views here.


def index(request):
    return HttpResponse("routinggggg appppppppppp")

@csrf_exempt
def create_route(request):
    if request.method == 'POST':
        try:
            route_data= JSONParser().parse(request)
            route_serializer=RouteSerializer(data=route_data)
            if route_serializer.is_valid():
                route_serializer.save()
                return HttpResponse("route created successfully", status=OK)
            else:
                return JsonResponse(route_serializer.errors, status=BAD_REQUEST)
        except JSONDecodeError as e:
            return HttpResponse("Invalid JSON data", status=BAD_REQUEST)
    else:
        return HttpResponse("Only POST method is allowed", status=METHOD_NOT_ALLOWED)
    
class CustomPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size' 
    max_page_size = 500
    
class RouteListAPIView(ListAPIView):
    queryset = Route.objects.all()     
    serializer_class = RouteSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['user_id' , 'route_id']  
    search_fields = ['route_id']