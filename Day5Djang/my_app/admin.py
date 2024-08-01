from django.contrib import admin
from .models import Category,Product
from django.contrib.auth.models import Group,User
# Register your models here.

# admin.site.register([Category,Product])

admin.site.unregister([])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["category_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","price","issue_year"]
    search_fields=["product_name","color"]
    list_filter=["price","cotegory_name","color","category",""]


