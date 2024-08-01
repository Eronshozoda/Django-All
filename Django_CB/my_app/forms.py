from django import forms
from .models import Teacher

class GForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'midle_name', 'subject', 'age']
