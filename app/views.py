from django.shortcuts import render
from django.contrib import messages
from app.models import *
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

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
        file = request.POST['file']
        contact = request.POST['contact']

        data = Booking(name=name,email=email,date=date,destination=destination,subject=subject,file=file,contact=contact)
        data.save()
        messages.success(request,'Booking Successfully...')

        subject = 'Touriest information which you can handle'
        message = f'This is your Touriest Which name is {name} and location is {destination} and contact is {contact}'
        recipient_list = ['yadavnain2525@gmail.com',]
        attachment_path = 'static/img/man1.jpg'

        email = EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipient_list)
        email.attach_file(attachment_path)
        email.send()

        # if __name__=="__main__":
        return render(request,'booking.html')
 
    return render(request,'booking.html')


def BookWithLink(request,location):
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        subject = request.POST['subject']
        file = request.POST['file']
        contact = request.POST['contact']

        data = Booking(name=name,email=email,date=date,destination=location,subject=subject,file=file,contact=contact)
        data.save()
        messages.success(request,'Booking Successfully...')

        data = Booking.objects.last()
        context = {
            'img':data.file,
        }

        subject = 'Touriest information which you can handle'
        message = f'This is your Touriest Which name is {name} and location is {location} and contact is {contact}'
        recipient_list = ['receiver email',]
        attachment_path = 'static/img/contact.jpg'

        email = EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipient_list)
        email.attach_file(attachment_path)
        email.send()

        return render(request,'BookWithLink.html')
    else:
        context = {
            'location':location
        }
        return render(request,'BookWithLink.html',context)