from django.shortcuts import render
from django.contrib import messages
from app.models import *

# Create your views here.
def index(request):
    popularDestinaion_data = popularDestinaion.objects.all()
    packages_data = packages.objects.all()
    guide_data = guide.objects.all()
    testimonial_data = testimonialModel.objects.all()
    return render(request,'index.html',{'popularDestinaion_data':popularDestinaion_data, 'packages_data':packages_data,'guide_data':guide_data,'testimonial_data':testimonial_data})


def about(request):
    guide_data = guide.objects.all()
    return render(request,'about.html',{'guide_data':guide_data})

def kutch(request):
    kutch_data = kutch_Tour.objects.all()
    return render(request,'kutch.html',{'kutch_data':kutch_data})

def nationalPark(request):
    NationalPark_data = NationalParks.objects.all()
    return render(request,'nationalParks.html',{'NationalPark_data':NationalPark_data})

def temples(request):
    temples_data = famousTemples.objects.all()
    return render(request,'temples.html',{'temples_data':temples_data})

def testimonial(request):
    testimonial_data = testimonialModel.objects.all()
    return render(request,'testimonial.html',{'testimonial_data':testimonial_data})

def team(request):
    guide_data = guide.objects.all()
    return render(request,'team.html',{'guide_data':guide_data})

def service(request):
    testimonial_data = testimonialModel.objects.all()
    return render(request,'service.html',{'testimonial_data':testimonial_data})

def package(request):
    packages_data = packages.objects.all()
    return render(request,'package.html',{'packages_data':packages_data})

def destination(request):
    popularDestinaion_data = popularDestinaion.objects.all()
    return render(request,'destination.html',{'popularDestinaion_data':popularDestinaion_data})

def booking(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        destination = request.POST['destination']
        subject = request.POST['subject']

        data = Booking(name=name,email=email,date=date,destination=destination,subject=subject)
        data.save()
    return render(request,'booking.html')


def BookWithLink(request,location):
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        subject = request.POST['subject']

        data = Booking(name=name,email=email,date=date,destination=location,subject=subject)
        data.save()
        messages.success(request,'Booking Successfully...')
        return render(request,'BookWithLink.html')
    else:
        context = {
            'location':location
        }
        return render(request,'BookWithLink.html',context)