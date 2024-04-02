"""
URL configuration for RentalAxis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from RA import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('login/', views.Signup, name='login'),
    path('about/', views.About, name='about'),
    path('register_rent/', views.Register_rent, name='register_rent'),
    path('register_sell/', views.Register_sell, name='register_sell'),
    path('donation/', views.Donation, name='donation'),
    path('chatbot/', views.Chatbot, name='bot'),
    path('contact/', views.Contact, name='contact'),
    path('users_list/', views.users, name='users_list'),
    path('users_list/details/<int:id>', views.details, name='details'),

]
