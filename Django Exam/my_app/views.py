from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import Job,Company,JobCategory

def read_users(request):
    model=Job.objects.all()
    return render(request,'jobs.html',{'jobs':model})
    


def create_job(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        company_id = request.POST.get('company')  
        category_id = request.POST.get('category')  

        model = Job.objects.create(
            title=title,
            description=description,
            salary=salary,
            company_id=company_id,
            category_id=category_id
        )
        model.save()
        return redirect('list-users')

    return render(request, 'jobs_create.html')


def delete_jobs(request,id):
    model=Job.objects.get(id=id)
    model.delete()
    return redirect("list-users")



def update_job(request, id):
    if request.method == 'POST':
        # Получаем обновленные данные из формы
        job = Job.objects.get(id=id)
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.salary = request.POST.get('salary')
        job.company_id = request.POST.get('company')  # ID компании из формы
        job.category_id = request.POST.get('category')  # ID категории из формы
        job.save()

        return redirect('list-users')

    job = Job.objects.get(id=id)
    return render(request, 'job_update.html', {'job': job})







def read_company(request):
    model=Company.objects.all()
    return render(request,'company.html',{'companies':model})






def create_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Company.objects.create(name=name, description=description)
        return redirect('companies_list') 
    return render(request, 'create_company.html')



def delete_company(request,id):
    user=Company.objects.get(id=id)
    user.delete()
    return redirect("companies_list")




def update_company(request,id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return redirect('companies_list') 
    
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.description = request.POST.get('description')
        company.address = request.POST.get('address')
        company.contact_info = request.POST.get('contact_info')
        company.save()
        return redirect('companies_list') 

    return render(request, 'update_company.html', {'company': company})

    

def read_job_category(request):
    model=Company.objects.all()
    return render(request,'category.html',{'categories':model})
























# from django.shortcuts import render,HttpResponseRedirect

# def read_users(request):
#     return render(request,'jobs.html')
    


# # views.py
# from django.views.generic import ListView
# from .models import Job

# class JobListView(ListView):
#     model = Job
#     template_name = 'jobs/job_list.html'  # Путь к HTML-шаблону
#     context_object_name = 'jobs'  # Имя переменной в контексте шаблона
