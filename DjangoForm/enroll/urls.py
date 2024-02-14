from django.urls import path
from . import views

urlpatterns = [
    path("",views.showformdata),
    path("user/",views.userdata),
]
