from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.aboutpage),
    path('contact/', views.contactpage),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.userlogout, name='logout'),
    path('addpost/', views.addpost, name='add'),
    path('updatepost/<int:id>', views.updatepost, name='update'),
    path('deletepost/<int:id>', views.deletepost, name='delete'),
    path('editprofile/<int:id>', views.editprofile, name='editprofile'),
]
