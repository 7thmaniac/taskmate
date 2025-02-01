from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from pathlib import Path

# Create your views here.

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit= False).owner = request.user
            form.save()
        messages.success(request,("New Task Added"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get("page")
        all_tasks = paginator.get_page(page)
        context = {'welcome_text':"Welcome to Todo List app", 'all_tasks':all_tasks}
        return render(request, 'todolist.html',context)
 
@login_required   
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted!, You are not owner of this task."))
    return redirect('todolist')

def index(request):
    context = {'index':'Welcome to Index Page'}
    return render(request, 'index.html',context)

@login_required
def completed(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("Access Restricted!, You are not owner of this task."))
    return redirect('todolist')

@login_required
def pending(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request,("Access Restricted!, You are not owner of this task."))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        edit_task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=edit_task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task successfully edited"))
        return redirect('todolist')
    else:
        edit_task = TaskList.objects.get(pk=task_id)
        context = {'welcome_text':"Welcome to Todo List app", 'edit_task':edit_task}
        return render(request, 'edit_task.html',context)
    
def contact_us(request):
    context = {'contact_us':'Please contact us at example@gmail.com and you can call us at +18001080700'}
    return render(request, 'contact_us.html',context)

def about_us(request):
    context= {'about_us':'This is information about_us'}
    return render(request, 'about_us.html',context)


