from django.contrib import admin
from .models import Contractor, Student, Teacher
# Register your models here.

class ContractorAdmin(admin.ModelAdmin):
    list_display= ('name', 'age', 'salary')
admin.site.register(Contractor, ContractorAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display= ('name', 'age', 'fees')
admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display= ('name', 'age', 'salary')
admin.site.register(Teacher, TeacherAdmin)
