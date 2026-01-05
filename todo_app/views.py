from django.shortcuts import render, redirect
from .models import Task

def home(request):
    # Get all tasks from database
    tasks = Task.objects.all().order_by('-created_at') 
    
    if request.method == 'POST':
        new_task = request.POST.get('task')
        if new_task:
            Task.objects.create(title=new_task)
        return redirect('home')

    return render(request, 'todo_app/home.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')