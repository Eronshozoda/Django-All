from django.shortcuts import render
from .models import Category,Video
from django.views import generic


class VideoListView(generic.ListView):
    model=Video
    template_name="video_list.html"




class VideoCreateView(generic.CreateView):
    model=Video
    fields="__all__"
    template_name="create_video.html"
    success_url="/"



class VideoUpdateView(generic.UpdateView):
    model=Video
    fields="__all__"
    template_name="update_video.html"
    success_url="/"



class VideoDeleteView(generic.DeleteView):
    model=Video
    template_name="delete_video.html"
    success_url="/"


class VideoDetailView(generic.DetailView):
    model=Video
    template_name="detail.html"
    succes_url="/"
    






class CategoryListView(generic.ListView):
    model=Category
    template_name="category_list.html"




class CategoryCreateView(generic.CreateView):
    model=Category
    fields="__all__"
    template_name="create_category.html"
    success_url="/"



class CategoryUpdateView(generic.UpdateView):
    model=Category
    fields="__all__"
    template_name="update_video.html"
    success_url="/"



class CategoryDeleteView(generic.DeleteView):
    model=Category
    template_name="delete_category.html"
    success_url="/"
    


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "detvid.html"

    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context["videos"] = Video.objects.filter(category=kwargs['object'])
            return context