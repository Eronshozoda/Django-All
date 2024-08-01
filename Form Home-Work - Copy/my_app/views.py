from django.shortcuts import render
from django.views import generic
from .models import Cars,Book

class CarsListView(generic.ListView):
    model=Cars
    template_name="cars_list.html"
    succes_url="/"


class CarsCreateView(generic.CreateView):
    model=Cars
    fields="__all__"
    template_name="create_cars.html"
    success_url="/"



class CarsUpdateView(generic.UpdateView):
    model=Cars
    fields="__all__"
    template_name="update_cars.html"
    success_url="/"

class CarsDeleteView(generic.DeleteView):
    model=Cars
    template_name="delete_cars.html"
    success_url="/"
    






class BookListView(generic.ListView):
    model=Book
    template_name="book_list.html"
    succes_url="/"


class BookCreateView(generic.CreateView):
    model=Book
    fields="__all__"
    template_name="create_book.html"
    success_url="/"



class BookUpdateView(generic.UpdateView):
    model=Book
    fields="__all__"
    template_name="update_book.html"
    success_url="/"

class BookDeleteView(generic.DeleteView):
    model=Book
    template_name="delete_book.html"
    success_url="/"
    
# class ModelDeleteViewBook(DeleteView):
#     model = Book
#     template_name = 'book_delete.html'
#     success_url = reverse_lazy('book_list')