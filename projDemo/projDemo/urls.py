"""
URL configuration for projDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from projDemo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('aboutus/', views.aboutus, name="about"),
    path('course/', views.course, name="course"),
    # path('course/<int:courseid>', views.courseDetails),
    # path('course/<str:courseid>', views.courseDetails),
    # path('course/<slug:courseid>', views.courseDetails),
    path('course/<courseid>', views.courseDetails),                 # if datatype is't specified
    path('contact/', views.contact, name= "contact")
]
