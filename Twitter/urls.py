"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterApp.views import hashtag_view, home_view, accounts_view, login_view, signup_view, logout_view, profile_view, splash_view

# links URL to view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_view, name="accounts_view"),
    path('home/', home_view, name="home_view"),

    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name="signup_view"),
    path('logout/', logout_view, name="logout_view"),

    path('profile/<username>/', profile_view, name="profile_view"),
    path('hashtag/', hashtag_view, name="hashtag_view"),
    path('splash/', splash_view, name="splash_view")
]
