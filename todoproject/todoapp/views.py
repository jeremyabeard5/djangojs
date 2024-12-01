from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo, BlogPost

# Create your views here.

## Render the home page
def index(request):
    return render(request, 'index.html')

## Render the todo page
def todo(request):
    return render(request, 'todo.html')

## Render the contact page
def contact(request):
    return render(request, 'contact.html')

## Render the services page
def services(request):
    return render(request, 'services.html')

## Render the Tableau page
def tableau(request):
    return render(request, 'tableau.html')

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

# List of all blog posts
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

# Single blog post detail view
def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog_detail.html', {'post': post})
