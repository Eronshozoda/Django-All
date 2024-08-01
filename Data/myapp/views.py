from django.shortcuts import render

def home_page(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about.html')

def user(request):
    user ={
        'name':"Kabir",
        'surname':"Ghafurov",
        "age":20,
        'course':"Python"
    }
    return render(request,'user.html',context=user)