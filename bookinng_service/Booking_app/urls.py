from django.contrib import admin
from django.urls import path
from Booking_app import views

urlpatterns = [
    path("", views.index , name='home'),
    path('bookings/', views.BookingListAPIView.as_view(), name='booking-list'),
    path("create", views.create , name='create'),
    path('booking/<str:ticket_id>/', views.BookingDetailAPIView.as_view(), name='booking-detail'),

]
