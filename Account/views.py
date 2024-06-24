from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import Profile

# Create your views here.
def register(request):

    if request.method == "POST":

        username = request.POST['username']
        name = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request , "Username Already Taken")
            return redirect('register')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request , "Email Already Used")
            return redirect('register')
        
        elif password != confirm_password:
            messages.info(request , "Password Not Matching")
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username , email=email , password=password )
            user.save()

            user_login = auth.authanticate(username=username , pasaword=password)
            auth.login(request , user_login)

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user = user_model , email_address=email , name=name)
            new_profile.save()
            return redirect('profile')

        

    context = {}
    return render(request , 'register.html' , context)