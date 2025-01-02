from django.shortcuts import render, redirect, get_object_or_404
from django.middleware.csrf import get_token
from django.core.mail import send_mail
#from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Todo, BlogPost, Media, ContactForm
from markdown import markdown
from .forms import ContactForm

# Create your views here.

## Render the home page
def index(request):
    print("views.py: index")
    return render(request, 'index.html')

## Render the schedule page
def schedule(request):
    print("views.py: schedule")
    return render(request, 'schedule.html')

## Render the todo page
def todo(request):
    print("views.py: todo")
    return render(request, 'todo.html')

## Render the contact page
#def contact(request):
#    print("views.py: contact")
#    return render(request, 'contact.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database

            # Send email
            send_mail(
                'New Contact Form Submission',
                'You have a new contact form submission from {} ({}) with the following message:\n\n{}'.format(
                    form.cleaned_data['name'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['message']
                ),
                'your-email@gmail.com',  # From email
                ['jeremyabeard5@gmail.com'],  # To email, can be a list to send to multiple recipients
                fail_silently=False,
            )

            return redirect('home')  # Redirects to the homepage after successful form submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

## Render the about us page
def about(request):
    print("views.py: about")
    return render(request, 'about.html')

## Render the services page
def services(request):
    print("views.py: services")
    return render(request, 'services.html')

## Render the Tableau page
def tableau(request):
    print("views.py: tableau")
    return render(request, 'tableau.html')

## Get all todos
def get_todos(request):
    print("views.py: get_todos")
    todos = list(Todo.objects.values())
    return JsonResponse({'todos': todos})

## Create a new todo
#@csrf_exempt
def add_todo(request):
    print("views.py: add_todo")
    csrf_token = get_token(request)
    print("CSRF Token from middleware:", csrf_token)
    print("CSRF Token from cookie:", request.COOKIES.get('csrftoken'))
    if request.method == 'POST':
        title = request.POST.get('title', '')
        todo = Todo.objects.create(title=title)
        return JsonResponse({'id': todo.id, 'title': todo.title, 'is_completed': todo.is_completed})
    
    return JsonResponse({'error': 'Only POST request is allowed'})

## Update a todo
def update_todo(request, id):
    print("views.py: update_todo")
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return JsonResponse({'id': todo.id, 'title': todo.title, 'is_completed': todo.is_completed})
    
    return JsonResponse({'error': 'Only POST request is allowed'})

## Delete a todo
def delete_todo(request, id):
    print("views.py: delete_todo")
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({'id': id})
    
    return JsonResponse({'error': 'Only POST request is allowed'})

# List of all blog posts
def blog_list(request):
    print("views.py: blog_list")
    posts = BlogPost.objects.all().order_by('-created_at')
    for post in posts:
        post.content_html = markdown(post.content, extensions=['fenced_code', 'tables'])
    return render(request, 'blog_list.html', {'posts': posts})

# Single blog post detail view
def blog_detail(request, id):
    print("views.py: blog_detail")
    post = get_object_or_404(BlogPost, id=id)
    post.content_html = markdown(post.content, extensions=['fenced_code', 'tables'])
    return render(request, 'blog_detail.html', {'post': post})

def media_feed(request):
    print("views.py: media_feed")
    photos = Media.objects.all().order_by('-uploaded_at')  # Latest first
    return render(request, 'media_feed.html', {'photos': photos})
