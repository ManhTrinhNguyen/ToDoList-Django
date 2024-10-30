from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo 
from .forms import TodoForm

# Create your views here.

def list_all_tasks(request):
  todos = Todo.objects.all()
  return render(request, 'todos.html', {'todos': todos})

def create_task(request):
  form = TodoForm()
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('todos')

  return render(request, 'create_task.html', {'form': form})

def update_task(request, pk):
  todo = get_object_or_404(Todo, pk = pk)
  form = TodoForm(instance=todo)

  if request.method == 'POST':
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      return redirect('todos')
    
  return render(request, 'create_task.html', {'form': form})


def delete_task(request, pk):
  todo = get_object_or_404(Todo, pk = pk)
  if request.method == 'POST':
    todo.delete()
    return redirect('todos')
  
  return render(request, 'delete_task.html', {'todo': todo})