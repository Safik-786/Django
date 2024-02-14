from django.contrib import admin
from enroll.models import User, UserCollage

# Register your models here.
@admin.register(User)
class ModelAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'password')
    
@admin.register(UserCollage)
class ModelAdmin(admin.ModelAdmin):
    list_display=('id', 'student_name', 'teacher_name', 'email','password')
