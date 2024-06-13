from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('kutch',views.kutch,name='kutch'),
    path('nationalPark/',views.nationalPark,name='nationalPark'),
    path('temples/',views.temples,name='temples'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('team/',views.team,name='team'),
    path('service/',views.service,name='service'),
    path('package/',views.package,name='package'),
    path('destination/',views.destination,name='destination'),
    path('booking/',views.booking,name='booking'),
    path('BookWithLink/<str:location>',views.BookWithLink,name='BookWithLink'),
]
