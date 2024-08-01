from django.urls import path
from .views import *

urlpatterns = [
    path('',CourceListView.as_view(),name="cource-list"),
    path('create/',CourceCreateView.as_view(),name="create-cource"),
    path('update/<int:pk>/',CourceUpdateView.as_view(),name="update-cource"),



    path('show',StudentListView.as_view(),name="student-list"),
    path('create-student',StudentCreateView.as_view(),name="create-students"),
    path('updateStud/<int:pk>/',StudentUpdateView.as_view(),name="update-students"),


]

