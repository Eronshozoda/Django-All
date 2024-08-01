from django.shortcuts import render
from django.views import generic
from .models import Cource,Student

class CourceListView(generic.ListView):
    model=Cource
    template_name="cource_list.html"
    succes_url="/"


class CourceCreateView(generic.CreateView):
    model=Cource
    template_name="create_cource.html"
    fields="__all__"
    success_url="/"


class CourceUpdateView(generic.UpdateView):
    model=Cource
    template_name="update_cource.html"
    fields="__all__"
    success_url="/"


class CourseDeleteView(generic.DeleteView):
    model=Cource
    template_name="delete_cource.html"
    success_url="/"







class StudentListView(generic.ListView):
    model=Student
    template_name="student_list.html"
    succes_url="/"


class StudentCreateView(generic.CreateView):
    model=Student
    template_name="create_students.html"
    fields="__all__"
    success_url="/"


class StudentUpdateView(generic.UpdateView):
    model=Student
    template_name="update_students.html"
    fields="__all__"
    success_url="/"


class StudentDeleteView(generic.DeleteView):
    model=Student
    template_name="delete_students.html"
    success_url="/"





