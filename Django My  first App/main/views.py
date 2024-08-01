from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h4>'Assalomu Aleykum'</h4>")

def client(request):
    return HttpResponse("<h6>In hast sahifai klient</h6>")


def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')
