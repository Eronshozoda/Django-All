from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import CustomUser

def read_users(request):
    model=CustomUser.objects.all()
    return render(request,'index.html',{'users':model})
    
# Create your views here.



def create_users(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        last_name=request.POST['lastname']
        age=request.POST['age']
        adress=request.POST['adress']
        email=request.POST['email']
        phone_number=request.POST['phone']
        image=request.POST['image']


        model=CustomUser(first_name=fname,
                         last_name=last_name,
                         age=age,
                         adress=adress,
                         email=email,
                         phonr_number=phone_number,
                         image=image)
        
        model.save()

        return redirect('list-users')
    
    return render(request,'create-user.html')




def delete_users(request,id):
    user=CustomUser.objects.get(id=id)
    user.delete()
    return redirect("list-users")



def update_user(request,id):
    user=CustomUser.objects.get(id=id)
    if request.method=="POST":
        user.first_name=request.POST['firstname']
        user.last_name=request.POST['lastname']
        user.age=request.POST['age']
        user.adress=request.POST['adress']
        user.email=request.POST['email']
        user.phonr_number=request.POST['phone']
        user.save()

        return redirect('list-users')
    return render(request,'update-user.html',{'users':user})









