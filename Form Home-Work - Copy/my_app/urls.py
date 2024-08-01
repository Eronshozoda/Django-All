from django.urls import path
from .views import *


urlpatterns = [
    path('',CarsListView.as_view(),name="car-list"),
    path('create/',CarsCreateView.as_view(),name="create-cars"),
    path('update/<int:pk>/',CarsUpdateView.as_view(),name="update-car"),
    path('delete/<int:pk>/',CarsDeleteView.as_view(),name="delete-cars"),
    
    path('book/',BookListView.as_view(),name="book-list"),
    path('book/create/',BookCreateView.as_view(),name="create-book"),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name="book-update"),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name="delete-book"),
]