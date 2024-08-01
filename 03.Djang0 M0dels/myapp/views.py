# from django.shortcuts import render,HttpResponseRedirect
# from .models import Tasks
# def news_home(request):
#     news=Tasks.objects.all()
#     return render(request,"Task.html",{'news': news})


from django.shortcuts import render, HttpResponse
from .models import Task

def news_home(request):
    news = Task.objects.all()
    return render(request, "Task.html", {'news': news})

# def create(request):
#     if request.method == 'POST':
#         # Обработка данных формы и создание новой задачи
#         title = request.POST.get('title')
#         due_date = request.POST.get('due_date')
#         user = request.POST.get('user')
#         Task.objects.create(title=title, due_date=due_date, user=user)
#         return HttpResponse("Задача успешно создана!")
#     return render(request, 'tasks/create_task.html')


