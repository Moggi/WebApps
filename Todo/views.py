from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Todo

def index(request):
    todoList = Todo.objects.all()[:10]

    context = {
        'todoList': todoList,
    }
    return render(request, 'Todo/index.html', context)

def details(request, id):
    todoItem = Todo.objects.get(id=id)

    context = {
        'todoItem': todoItem,
    }
    return render(request, 'Todo/details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todoItem = Todo(title=title, text=text)
        todoItem.save()

        return redirect('/todo')
    else:
        return render(request, 'Todo/add.html')
