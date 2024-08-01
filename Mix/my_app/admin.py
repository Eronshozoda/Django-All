from django.contrib import admin
from .models import Category,Video

admin.site.register([Category,Video])