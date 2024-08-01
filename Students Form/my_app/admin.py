from django.contrib import admin
from .models import Cource,Student


class CourceAdmin(admin.ModelAdmin):
    list_display=[
        "name",
    ]

class StudentAdmin(admin.ModelAdmin):
    list_display=[
        "cource",
        "fullname",
        "lastname",
        "age",
        "photo",
        "email",
    ]

admin.site.register(Cource,CourceAdmin)
admin.site.register(Student,StudentAdmin)

