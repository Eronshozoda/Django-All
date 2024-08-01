from django.shortcuts import render
from django.views import generic
from .models import Company,Product

class CompanyListView(generic.ListView):
    model=Company
    template_name="company_list.html"
    
class CompanyCreateView(generic.CreateView):
    model=Company
    template_name="create-company.html"
    fields="__all__"
    success_url="/"


class CompanyUpdateView(generic.UpdateView):
    model=Company
    template_name="update-company.html"
    fields="__all__"
    success_url="/"

class CompanyDeleteView(generic.DeleteView):
    model=Company
    template_name="delete-company"
    success_url="/"
