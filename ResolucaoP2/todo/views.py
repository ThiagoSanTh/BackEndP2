from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView
# Create your views here.


class todoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    