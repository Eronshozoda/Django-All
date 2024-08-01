from django.urls import path
from .views import *


urlpatterns = [
    path("",EmployeeListView.as_view(),name='employee-list'),
    path('create',EmployeeCreateView.as_view(),name='employee-create'),
    path('edit/<int:pk>',EmployeeUpdateView.as_view(),name='employee-edit'),
    

]
