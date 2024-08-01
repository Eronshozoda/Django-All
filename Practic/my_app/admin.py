from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'midle_name', 'subject', 'age']
    search_fields = ['first_name', 'last_name', 'subject']
    list_filter = ['subject', 'age']
