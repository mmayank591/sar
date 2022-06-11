from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('mail', views.mail, name='mail'),
    path('link',views.link,name='link'),
    path('home1',views.home1,name='home1'),
]
