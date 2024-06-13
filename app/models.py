from django.db import models

# Create your models here.

class famousTemples(models.Model):
    image = models.ImageField(upload_to='Temples')
    location = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    search_name = models.CharField(max_length=100)
    visit = models.BigIntegerField()
    heading = models.CharField(max_length=300)
    rating = models.DecimalField(decimal_places=1,max_digits=3)


class testimonialModel(models.Model):
    image = models.ImageField(upload_to='testimonial')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    para = models.TextField(max_length=300)


class packages(models.Model):
    image = models.ImageField(upload_to='packages')
    location = models.CharField(max_length=100)
    days = models.IntegerField()
    search_name = models.CharField(max_length=100)
    person = models.IntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    heading = models.CharField(max_length=300)

class guide(models.Model):
    image = models.ImageField(upload_to='guide')
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
 
class  popularDestinaion(models.Model):
    image = models.ImageField(upload_to='PopularDestination')
    nameOfImage = models.CharField(max_length=100)
    search_name = models.CharField(max_length=100)
    discount = models.IntegerField()

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    subject = models.TextField(max_length=200)
    file = models.ImageField(upload_to='bookingImage')
    contact = models.BigIntegerField()

class kutch_Tour(models.Model):
    image = models.ImageField(upload_to='kutch_Tour')
    location = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    search_name = models.CharField(max_length=100)
    visit = models.BigIntegerField()
    heading = models.CharField(max_length=300)
    rating = models.DecimalField(decimal_places=1,max_digits=3)

class NationalParks(models.Model):
    image = models.ImageField(upload_to='NationalParks')
    location = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    search_name = models.CharField(max_length=100)
    visit = models.BigIntegerField()
    heading = models.CharField(max_length=300)
    rating = models.DecimalField(decimal_places=1,max_digits=3)
