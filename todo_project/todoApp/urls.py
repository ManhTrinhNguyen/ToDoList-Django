from django.urls import path 
from . import views

urlpatterns = [
  path('todos/', views.list_all_tasks, name='todos'),
  path('todos/new/', views.create_task, name='create_task'),
  path('todos/<int:pk>/edit/', views.update_task, name='update_task'),
  path('todos/<int:pk>/delete/', views.delete_task, name='delete_task')
]