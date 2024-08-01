from django.urls import path
from my_app.views import MyView,GeeksCreate

urlpatterns = [

	path('about/', MyView.as_view()),
    path('',GeeksCreate.as_view()),

]

