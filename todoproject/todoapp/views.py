from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo

# Create your views here.

## Render the home page
def index(request):
    return render(request, 'index.html')

## Get all todos
def get_todos(request):
    todos = list(Todo.objects.values())
    return JsonResponse({'todos': todos})

## Create a new todo
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        todo = Todo.objects.create(title=title)
        return JsonResponse({'id': todo.id, 'title': todo.title, 'is_completed': todo.is_completed})
    
    return JsonResponse({'error': 'Only POST request is allowed'})

## Update a todo
def update_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return JsonResponse({'id': todo.id, 'title': todo.title, 'is_completed': todo.is_completed})
    
    return JsonResponse({'error': 'Only POST request is allowed'})

## Delete a todo
def delete_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({'id': id})
    
    return JsonResponse({'error': 'Only POST request is allowed'})
