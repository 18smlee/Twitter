from django.shortcuts import render

# Create your views here.

def hashtag(request):
    return render(request, 'hashtag.html', {})

def home(request):
    return render(request, 'home.html', {})

def login_signup(request):
    return render(request, 'login_signup.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def splash(request):
    return render(request, 'splash.html', {})
    
