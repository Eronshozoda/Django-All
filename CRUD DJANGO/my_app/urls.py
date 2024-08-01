from django.urls import path
from .views import read_users,create_users,delete_users,update_user


urlpatterns = [
    path('',read_users,name="list-users"),
    path('create_user/',create_users,name='create-user'),
    path('delete-user/<id>',delete_users, name='delete-user'),   
    path('update-user/<id>',update_user,name='update-user'),


]


