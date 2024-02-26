from django.contrib import admin
from .models import Post, PostwithImage
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'author', 'title']
admin.site.register(Post, PostModelAdmin)
    
class PostModelAdmin2(admin.ModelAdmin):
    list_display= ['id', 'author', 'title', 'blog_image']
admin.site.register(PostwithImage, PostModelAdmin2)
    
    

