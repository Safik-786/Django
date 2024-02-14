from django.urls import path
from . import views

urlpatterns = [
    path("",views.showformdata),
    path("widget/",views.widget),
    path("form/",views.form),
    path("success",views.thankyou)
]
