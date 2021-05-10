from django.contrib import admin
# from django.utils.html import mark_safe
from .models import *


# from .forms import UserCreationForm
# from .models import MyUser

class ColorAdmin(admin.ModelAdmin):
	list_display = ('id','color')

admin.site.register(Color, ColorAdmin)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


admin.site.register(Category, CategoryAdmin)


# class ImagesInline(admin.TabularInline):
#     fk_name = 'product'
#     # model = Images


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price","image",)
    # readonoly_fields = ImagesInline
    # inlines = [ImagesInline, ]


# "get_image"
admin.site.register(Product, ProductAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "size",)


admin.site.register(Size, SizeAdmin)

admin.site.site_header = 'Sonun Fashion'

admin.site.register(Stock)