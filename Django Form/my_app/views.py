from django.shortcuts import render
from django.views import generic
from .models import Employee

class EmployeeListView(generic.ListView):
    model=Employee
    template_name="employee_list.html"



class EmployeeCreateView(generic.CreateView):
    model=Employee
    fields="__all__"
    template_name="create_employee.html"
    success_url="/"



class EmployeeUpdateView(generic.UpdateView):
    model=Employee
    template_name="employee_edit.html"
    fields="__all__"
    success_url="/"