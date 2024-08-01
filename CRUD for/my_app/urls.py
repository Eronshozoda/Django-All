from django.urls import path
from .views import *

urlpatterns = [
    path('',CompanyListView.as_view(),name='company-list'),
    path('create/',CompanyCreateView.as_view(),name='create-company'),
    path('update/<int:pk>/',CompanyUpdateView.as_view(),name='update-company'),
    
]
