from django.shortcuts import render
# from .models import Person
def news_home(request):
    # news=Person.objects.all()
    return render(request,"index.html")
