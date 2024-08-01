from django.contrib import admin
from .models import CustomerUser, Tasks
# from django.contrib.auth.models import Group,User

# Register your models here.
# admin.site.unregister([Group,User])

admin.site.register([CustomerUser, Tasks])
