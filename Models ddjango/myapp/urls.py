from django.urls import path
from . import views


urlpatterns = [
    # path('home',views.home_page),
    # path("about",views.about),
    path('',views.news_home,name='news-page'),
]