from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profile' , request.user.username)

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

            user_login = auth.authenticate(username=username , password=password)
            auth.login(request , user_login)

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user = user_model , email_address=email , name=name)
            new_profile.save()
            return redirect('profile' , user_model.username)

        

    context = {}
    return render(request , 'register.html' , context)

@login_required(login_url='login')
def profile(request , username):

    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)

    user_object2 = User.objects.get(username=request.user)
    user_profile2 = Profile.objects.get(user=user_object2)

    context = { "user_profile" : user_profile , "user_profile2": user_profile2}
    return render(request , 'profile.html' , context)

def login(request):

    if request.user.is_authenticated:
        return redirect('profile' , request.user.username)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request , user)
            return redirect('profile' , username)
            
        else:
            messages.info(request , "Account not found!")
            return redirect('login')

    return render(request , 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')