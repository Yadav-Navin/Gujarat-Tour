from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from authenticate.forms import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('profile')
        else:
            # Return an 'invalid login' error message.
            messages.info(request, ("Invalid Login, Try Again."))
            return redirect('login')
    
    else:
        return render(request,'login.html', {})


    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfull !!"))
    return redirect('index')

# def register_user(request):
    # if request.method == 'POST':

    #     form = RegisterUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password1']
    #         user = authenticate(username=username,password=password)
    #         login(request, user)

            # mydict = {'username':username}
            # user.save()
            # html_template = 'register_email.html'
            # html_message = render_to_string(html_template,context=mydict)
            # subject = 'Welcome to Gujarat Website'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email]
            # message = EmailMessage(subject,html_message,email_from,recipient_list)
            # message.content_subtype = 'html'
            # message.send()
            # return redirect("login")

            # mail send
            # try:
            #     subject = 'welcome to Gujarat Travel Website'
            #     message = f'Hi {user.username}, Thank you for registration in Gujarat Travel Website'
            #     recipient_list = [user.email,]
            #     send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=recipient_list)
            # except BadHeaderError:
            #     messages.error(request, ("Invalid Header Found !!"))
            #     return redirect('profile')

            # messages.success(request, ("Registration Successfull !!"))
            # return redirect('profile')
    # else:
    #     form = RegisterUserForm()
    # return render(request,'register.html', {'form':form,})

def register_user(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is alredy Exists')
            return redirect({'register'})
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is alredy Exists')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username,password=password,email=email
            )
            mydict = {'username':username}
            user.save()
            html_template = 'register_email.html'
            html_message = render_to_string(html_template,context=mydict)
            subject = 'Welcome to Gujarat Website'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject,html_message,email_from,recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect("login")
    else:
        return render(request, 'register.html')        



@login_required
def profile_user(request):
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'editprofile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        data = contact_user(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request, ("Message Send Successfully..."))
        return redirect('contact')
    else:
        return render(request,'contact.html')