from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User
from Account.models import Profile


def home(request):
    if request.user.is_authenticated:

        user_object2 = User.objects.get(username=request.user)
        user_profile2 = Profile.objects.get(user=user_object2)

        context = {"user_profile2" : user_profile2}
        return render(request , 'home.html' , context)
    
    else:
        context={}
        return render(request , 'home.html' , context)

