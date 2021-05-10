from django.contrib import admin
from .models import *
from django.db import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "city", "email", "phone", "created", "updated",)
admin.site.register(Order , OrderAdmin)