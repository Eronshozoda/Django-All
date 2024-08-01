# from django.urls import path
# from . import views

# urlpatterns = [
#     path('home', views.home_page,name="home-page"),
#     path('user',views.user_page,name="user-page"),
#     path('course',views.course_page,name="course-page"),
# ]

from django.urls import path
from .views import home_page,about_us,user

urlpatterns = [
    path("home",home_page,name='homepage'),
    path("aboutus",about_us,name='about'),
    path("user",user,name='user')
]