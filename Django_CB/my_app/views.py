from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Teacher

class GCraete(CreateView):
    model = Teacher
    template_name = "index.html"
    fields = ['first_name', 'last_name', 'midle_name', 'subject', 'age']
    success_url = '/tichlist/'

class TeacherListView(ListView):
    model = Teacher
    template_name = "tichlist.html"
    context_object_name = 'teacher_create'

class UpdateTeacherView(UpdateView):  
    model = Teacher
    template_name = "update.html"  
    fields = ['first_name', 'last_name', 'midle_name', 'subject', 'age']
    success_url = '/tichlist/'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Teacher, id=id_)

class DeleteTeacher(DeleteView):
    model = Teacher
    template_name = "delet.html"
    success_url = '/tichlist/'
