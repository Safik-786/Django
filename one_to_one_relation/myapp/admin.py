from django.contrib import admin
from .models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display= ('user', 'page_name', 'page_cat', 'page_publish_date')

admin.site.register(Page, PageAdmin)
