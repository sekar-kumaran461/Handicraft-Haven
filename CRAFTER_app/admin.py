from django.contrib import admin
from .models import *

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','image','description','created_at']
admin.site.register(Category)
admin.site.register(Product)





    