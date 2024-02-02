
from django.contrib import admin
from django.urls import path
from BookingApp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("signUp",views.signUp,name='signUp'),
    path("login", views.login, name='login'),
    path("index", views.index, name='index'),
    path("userPage",views.userPage,name='userPage'),
    path("ambulancePage",views.ambulancePage,name="ambulancePage"),
    path("hospitalPage",views.hospitalPage,name="hospitalPage"),
    path("am_booking",views.am_booking,name="am_booking"),
    path("patient1",views.patient1,name="patient1"),
    path("hos_bookingform",views.hos_bookingform,name="hos_bookingform"),
    path("hos_patient1",views.hos_patient1,name="hos_patient1"),
    path("view_amb_booking",views.view_amb_booking,name="view_amb_booking"),
    path("view_hos_booking",views.view_hos_booking,name="view_hos_booking"),
    path("avHospital",views.avHospital,name="avHospital"),
    path("avAmbulance",views.avAmbulance,name="avAmbulance"),
    path("hos_view",views.hos_view,name="hos_view"),
    path("amb_view",views.amb_view,name="amb_view"),
    path("nearby_hos",views.nearby_hos,name="nearby_hos"),
    path("nearby_hos_usr",views.nearby_hos_usr,name="nearby_hos_usr"),
    path("search_hospital",views.search_hospital,name="search_hospital"),
    path("enter_city",views.enter_city,name="enter_city"),
    path("emergency_create",views.emergency_create,name="emergency_create"),
    path("emg_booking",views.emg_booking,name="emg_booking"),

]
