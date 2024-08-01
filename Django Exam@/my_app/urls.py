from django.urls import path
from .views import read_users


urlpatterns = [
    path('salom',read_users,name="list-users"),
    


]


