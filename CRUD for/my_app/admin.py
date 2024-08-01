from django.contrib import admin
from .models import Company,Product

admin.site.register([Company,Product])