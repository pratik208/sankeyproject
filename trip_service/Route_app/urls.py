from django.contrib import admin
from django.urls import path
from Route_app import views

urlpatterns = [
    path("", views.index, name='home'),
    path("/create", views.create_route, name='create_route'),  
    path("/list/", views.RouteListAPIView.as_view(), name='route-list'),  
]
