from django.contrib import admin
from .models import Company,JobCategory,Job


# admin.site.register([Company,JobCategory,Job])

@admin.register(JobCategory)
class JobCategory(admin.ModelAdmin):
    list_display=["name"]




@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=["name","address","contact_info"]



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=["title","description","salary","company"]
    search_fields=["title","salary","category"]
    list_filter=["title","salary","company",]


#Baroi unregister kadan

# admin.site.unregister([Group,User])