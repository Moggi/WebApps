from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render, redirect

from .apps import HomeConfig

def index(request):

    context = getContext({
        'pageTitle': 'WebApp - Home'
    })
    return render(request, 'Home/index.html', context)

def getContext(updatedDict):
    context = dict()
    context['appName'] = HomeConfig.name
    context['pageTitle'] = HomeConfig.name

    context.update(updatedDict)
    return context
