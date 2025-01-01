from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('todo/', views.todo, name='todo'),
    path('tableau/', views.tableau, name='tableau'),
    path('get_todos/', views.get_todos, name='get_todos'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update_todo/<int:id>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('media/', views.media_feed, name='media_feed'),
    path('about/', views.about, name='about'),
]
