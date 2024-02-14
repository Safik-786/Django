from enroll import views
from django.urls import path, include

urlpatterns = [
    path('', views.AddShow, name='addandshow' ),
    path('update/<int:id>', views.update, name='updatedata' ),
    path('delete/<int:id>', views.deleteData, name='deletedata' )
]
