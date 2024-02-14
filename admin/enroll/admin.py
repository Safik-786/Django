from django.contrib import admin
from enroll.models import Student, Product
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail', 'stuepass')
@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display=('prodid','prodname','prodprice', 'discount','prodimage')

# admin.site.register(Student, StudentAdmin)