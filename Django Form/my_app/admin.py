from django.contrib import admin
from .models import Employee



# # @admin.register(Employee)
# admin.site.register(Employee,EmployeeAdmin):    

class EmployeeAdmin(admin.ModelAdmin):
    list_display=[
        "fullname",
        "address",
        "email",
        "gender"]
        
admin.site.register(Employee,EmployeeAdmin)

