from django.contrib import admin
from .models import CustomerUser,Tasks
 

admin.site.register([CustomerUser,Tasks])