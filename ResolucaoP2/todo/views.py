from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.


class todoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    
class todoCreate(CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class todoUpdate(UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')
