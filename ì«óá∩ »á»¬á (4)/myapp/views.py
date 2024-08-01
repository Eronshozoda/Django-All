from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseNotFound
from .models import Tasks
# Create your views here.

def index(request):
    task=Tasks.objects.all()
    return render(request,'index.html', {'task':task})
