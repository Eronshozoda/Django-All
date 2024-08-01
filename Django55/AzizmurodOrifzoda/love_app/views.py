from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponseNotFound
from .models import CustomerUser

def read_users(request):
    model = CustomerUser.objects.all()
    return render(request, 'index.html', {'users': model})


def create_users(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        adress=request.POST['adress']
        email=request.POST['email']
        phone=request.POST['phone']
        
        model = CustomerUser(fname=fname,
                             lname=lname,
                             age=age,
                             adress=adress,
                             email=email,
                             phone_number=phone,)
        model.save()

        return redirect('list-users')
    
    return render (request, "create.html")


def delate_users(request, id):
    user = CustomerUser.objects.get(id=id)
    user.delete()
    return redirect("list-users")

def update_user(request, id):
    user = CustomerUser.objects.get(id=id)
    if request.method == "POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.age=request.POST['age']
        user.adress=request.POST['adress']
        user.email=request.POST['email']
        user.phone_number=request.POST['phone']
        user.save()

        return redirect('list-users')
    return render(request, 'update.html', {'users': user})


def home_user(request):

    return render(request, 'home.html')

def add_task(request):

    return render(request, 'add_task.html')

