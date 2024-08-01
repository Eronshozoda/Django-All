from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *

urlpatterns = [
    path('',VideoListView.as_view(),name='video-list'),
    path('video/create/',VideoCreateView.as_view(),name="create-video"),
    path('video/update/<int:pk>/', VideoUpdateView.as_view(), name="video-update"),
    path('video/delete/<int:pk>/', VideoDeleteView.as_view(), name="delete-book"),

    path('categories/',CategoryListView.as_view(),name='category-list'),
    path('category/create/',CategoryCreateView.as_view(),name="create-category"),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name="category-update"),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="delete-category"),


    path('video/detail/<int:pk>/', VideoDetailView.as_view(), name="detail-video"),
    path('categories/det/<int:pk>',CategoryDetailView.as_view(),name='detail-cat')









]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
