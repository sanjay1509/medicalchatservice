"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. adddata the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('userreg/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('ulogin/', views.userlogindef, name="userlogindef"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhomedef"),
    path('userlogout/', views.userlogoutdef, name="userlogoutdef"),
    path('adminlogout/', views.adminlogout, name="userlogoutdef"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('upload/', views.upload, name="upload"),
    path('upload1/', views.upload1, name="upload1"),
    path('upload2/', views.upload2, name="upload2"),
    path('adddata/', views.adddata, name="adddata"),
    path('adddoctor/', views.adddoctor, name="adddoctor"),
    path('viewdoc/', views.viewdoc, name="viewdoc"),
    path('addquery/', views.addquery, name="addquery"),


    path('training/', views.training, name="training"),
    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('nntrain/', views.nntrain, name="nntrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('testing/', views.testing, name="testing"),
    path('viewacc/', views.viewacc, name="viewacc"),
    path('viewapp/', views.viewapp, name="viewapp"),
    path('uviewapp/', views.uviewapp, name="uviewapp"),
    




    path('chatpage/', views.chatpage, name="chatpage"),
    path('chatpage2/', views.chatpage2, name="chatpage2"),
    path('chataction/', views.chataction, name="chataction"),
    path('moredetails/', views.moredetails, name="moredetails"),
    path('moredetails2/', views.moredetails2, name="moredetails2"),
    path('moredetails3/', views.moredetails3, name="moredetails3"),
    path('getmesg/', views.getmesg, name="getmesg"),  

    

    
]
