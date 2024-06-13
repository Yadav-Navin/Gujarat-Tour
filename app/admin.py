from django.contrib import admin
from .models import *       
# Register your models here.

@admin.register(famousTemples)
class famousTemplesAdmin(admin.ModelAdmin):
    list_display = ['id','image','location','price','search_name','visit','heading','rating']


@admin.register(kutch_Tour)
class kutch_TourAdmin(admin.ModelAdmin):
    list_display = ['id','image','location','price','search_name','visit','heading','rating']


@admin.register(NationalParks)
class NationalParksAdmin(admin.ModelAdmin):
    list_display = ['id','image','location','price','search_name','visit','heading','rating']


@admin.register(testimonialModel)
class testimonialAdmin(admin.ModelAdmin):
    list_display = ['id','image','name','location','para']


@admin.register(packages)
class packagesAdmin(admin.ModelAdmin):
    list_display = ['id','image','location','days','search_name','person','price','heading']


@admin.register(guide)
class guideAdmin(admin.ModelAdmin):
    list_display = ['id','image','name','experience']


@admin.register(popularDestinaion)
class PopularDestinationAdmin(admin.ModelAdmin):
    list_display = ['id','image','nameOfImage','search_name','discount']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','date','destination','subject','file','contact']