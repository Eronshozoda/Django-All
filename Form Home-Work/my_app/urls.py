from django.urls import path
from .views import *


urlpatterns = [
    path('',CategoryListView.as_view(),name="car-list"),
    path('create/',CategoryCreateView.as_view(),name="create-cars"),
    path('update/<int:pk>/',CategoryUpdateView.as_view(),name="update-car"),
    path('delete/<int:pk>/',CategoryDeleteView.as_view(),name="delete-cars"),
    
    path('book/',ProductListView.as_view(),name="book-list"),
    path('book/create/',ProductCreateView.as_view(),name="create-book"),
    path('book/update/<int:pk>/', ProductUpdateView.as_view(), name="book-update"),
    path('book/delete/<int:pk>/', ProductDeleteView.as_view(), name="delete-book"),
]