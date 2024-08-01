from django.urls import path
from .views import *

urlpatterns = [
    path('', GCraete.as_view(), name='teacher_create'),
    path('tichlist/', TeacherListView.as_view(), name='teacher_list'),
    path('update/<int:pk>/',UpdateTeacherView.as_view(),name = 'update_techer'),
    path('delete/<int:pk>/', DeleteTeacher.as_view(), name='teacher_delete'),  # Added URL for delete view
]

