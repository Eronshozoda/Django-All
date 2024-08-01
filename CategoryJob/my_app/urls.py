from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *

urlpatterns = [
    path('',JobListView.as_view(),name='job-list'),
    path('video/create/',JobCreateView.as_view(),name="job-video"),
    path('video/update/<int:pk>/', JobUpdateView.as_view(), name="job-update"),
    path('video/delete/<int:pk>/', JobDeleteView.as_view(), name="delete-job"),

]