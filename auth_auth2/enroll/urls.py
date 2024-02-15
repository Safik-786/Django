from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.signup , name='signup'),
    path('login/',views.userLogin, name='login'),
    path('profile/',views.userprofile),
    path('logout/',views.userLogout, name='logout'),
    path('changepass/',views.userChangePass, name='changepass'),
    path('userdetail/<int:id>',views.userDetail, name='userdetail'),
]
