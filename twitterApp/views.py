from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from twitterApp.models import Tweet

# Create your views here.

def hashtag_view(request):
    return render(request, 'hashtag.html', {})

def home_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'home.html', {'tweets': tweets})

def accounts_view(request):
    return render(request, 'accounts.html', {})
    
def login_view(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home_view')
    else:
        return redirect('accounts_view')

def signup_view(request):
    print(request.POST['username'], request.POST['password'], request.POST['email'])
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email']
        )
    login(request, user)
    return redirect('home_view')

def logout_view(request):
    logout(request)
    return redirect('accounts_view')

def profile_view(request):
    return render(request, 'profile.html', {})

def splash_view(request):
    return render(request, 'splash.html', {})
    
