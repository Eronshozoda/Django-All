from django.urls import path
from .views import read_users, create_users, delate_users, update_user, home_user, add_task

urlpatterns = [
    path('', read_users, name="list-users"),
    path('create_users/', create_users, name='create-users'),
    path('delate-user/<id>' , delate_users, name='delate-users'),
    path("update-user/<id>", update_user, name='update-user' ),
    path("home-user", home_user, name='home-user' ),
    path("add-task", add_task, name='add-task')
]