from django.shortcuts import render
from django.views import generic
from .models import Category,Product

class CategoryListView(generic.ListView):
    model=Category
    template_name="category_list.html"
    succes_url="/"


class CategoryCreateView(generic.CreateView):
    model=Category
    fields="__all__"
    template_name="create_category.html"
    success_url="/"



class CategoryUpdateView(generic.UpdateView):
    model=Category
    fields="__all__"
    template_name="update_category.html"
    success_url="/"

class CategoryDeleteView(generic.DeleteView):
    model=Category
    template_name="delete_category.html"
    success_url="/"
    






class ProductListView(generic.ListView):
    model=Product
    template_name="product_list.html"
    succes_url="/"


class ProductCreateView(generic.CreateView):
    model=Product
    fields="__all__"
    template_name="create_product.html"
    success_url="/"



class ProductUpdateView(generic.UpdateView):
    model=Product
    fields="__all__"
    template_name="update_product.html"
    success_url="/"

class ProductDeleteView(generic.DeleteView):
    model=Product
    template_name="delete_product.html"
    success_url="/"
    
# class ModelDeleteViewBook(DeleteView):
#     model = Book
#     template_name = 'book_delete.html'
#     success_url = reverse_lazy('book_list')