from django.urls import path
from . import views 


urlpatterns = [
    path('', views.read_users, name="list-users"),
    path('jobs/create/', views.create_user, name="create-job"),     
]