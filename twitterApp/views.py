from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from twitterApp.models import Tweet, Hashtag
import re

# Create your views here.

def hashtag_view(request, tagTitle):
    hashtag = Hashtag.objects.get(title=tagTitle)
    tweetsWithTag = Tweet.objects.filter(tags__title=hashtag.title)
    print("tweets with this tag", tweetsWithTag)
    return render(request, 'hashtag.html', {'hashtag': hashtag, 'tweetsWithTag': tweetsWithTag})

def home_view(request):
    hashtags = Hashtag.objects.all()
    tweets = Tweet.objects.all()

    hashtagTitles =[]
    for hashtag in hashtags:
        hashtagTitles.append(hashtag.title)
    
    if request.method == 'POST':
        tweet = Tweet.objects.create(
            author=request.user,
            body=request.POST['tweetBody']
        )
        # parsing through tweet body to create hashtags
        tweetBody = tweet.body
        tweetTags = re.findall(r"#(\w+)", tweetBody)
        for tag in tweetTags:
            if tag not in hashtagTitles:
                print(tag, "not in ", hashtags)
                newTag = Hashtag.objects.create(title=tag)
                tweet.tags.add(newTag)
            else:
                tweet.tags.add(tag)
        
    return render(request, 'home.html', {'tweets': tweets, 'hashtags': hashtags})

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

def profile_view(request, username):
    user = User.objects.get(username=username)
    tweets = Tweet.objects.all()
    userTweets = []

    for tweet in tweets:
        if tweet.author == user:
            userTweets.append(tweet)

    return render(request, 'profile.html', {'user': user, 'userTweets': userTweets})

def splash_view(request):
    return render(request, 'splash.html', {})
    
