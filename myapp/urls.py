"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from .views import *
import emp.views as fun
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', fun.home, name='home'),
    path('register/',fun.register_user, name='register'),
    path('random-fact/', random_fact_view, name='random_fact'),
    path('change_password/', fun.change_password, name='change_password'),
     path('logout/',fun.logout_user, name='logout'),
     path('navbar/',fun.navbar, name='navbar'),
    path("home",fun.emp_home),
    path("index/",fun.emp_home),
    # path("about/",about),
    # path("services/",services),
    path("emp/",include('emp.urls'))
]
