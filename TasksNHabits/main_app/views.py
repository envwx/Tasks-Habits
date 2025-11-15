from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = 'invalid sign up - try again'
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html',context)

@login_required
def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/task_details.html', {'task': task})

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    else:
        form = TaskForm()
    return render(request, 'tasks/form.html', {'form': form})

@login_required
def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user != request.user:
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_details', task_id=task.id)

    else:
        form = TaskForm(instance=task)

        return render(request, 'tasks/form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user == request.user:
        task.delete()
        return redirect('task_list')

@login_required
def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user == request.user:
        task.is_completed = True
        task.save()
        return redirect('task_details', task_id=task.id)
