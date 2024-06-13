from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    birthdate = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField()

    def str(self): 
        return f"{self.fname,self.lname,self.email}"

class contact_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=200)