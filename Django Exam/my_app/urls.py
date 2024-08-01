from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_users, name="list-users"),
    path('jobs/create/', views.create_job, name="create-job"), 
    path('delete-jobs/<id>',views.delete_jobs,name="delete-jobs"),
    path('update-job/<id>',views.update_job,name='update-job'),

    path('companies/', views.read_company, name='companies_list'),
    path('create_company/', views.create_company, name='create_company'),
    path('delete_company/<id>/',views.delete_company,name='delete-company'),
    path('update_company/<id>/',views.update_company,name='update_company'),

    path('all/', views.read_job_category, name='job_category'),
    

# job_category/



    
]



