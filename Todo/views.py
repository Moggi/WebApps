from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render, redirect

from .models import Todo
from .apps import TodoConfig

# ==============================================================================
# URL methods
# ==============================================================================
def index(request):
    todoList = Todo.objects.all()[:10]

    context = getContext({
        'pageTitle': 'WebApp - Todos',
        'todoList': todoList,
    })
    return render(request, 'Todo/index.html', context)

def details(request, id):
    todoItem = Todo.objects.get(id=id)

    context = getContext({
        'todoItem': todoItem,
    })
    return render(request, 'Todo/details.html', context)

def add(request):
    context = getContext()

    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todoItem = Todo(title=title, text=text)
        todoItem.save()

        return redirect('/todo')
    else:
        return render(request, 'Todo/add.html', context)


# ==============================================================================
# POST Only methods
# ==============================================================================
def delete(request):
    if(request.method == 'POST'):
        todoItemId = request.POST['todoItemId']

        todoItem = Todo.objects.get(id=todoItemId)
        todoItem.delete()

    return redirect('/todo')


# ==============================================================================
# Utilities
# ==============================================================================
def getContext(updatedDict={}):
    context = dict()
    context['appName'] = TodoConfig.name
    context['pageTitle'] = TodoConfig.name

    context['navList'] = [
        {
            'url': 'add',
            'title': 'Add a Todo',
        },
    ]

    context.update(updatedDict)
    return context
