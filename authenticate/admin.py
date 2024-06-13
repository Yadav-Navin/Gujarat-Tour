from django.contrib import admin
from authenticate.models import *

# Register your models here.

@admin.register(contact_user)
class contact_userAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['id','user','fname','lname','bio','email','birthdate','contact','address']
