from django.contrib import admin
from .models import CustomUser,Tasks
from django.contrib.auth.models import Group,User


admin.site.register([CustomUser,Tasks])


#Baroi unregister kadan

# admin.site.unregister([Group,User])