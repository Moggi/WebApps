from django.http import HttpResponse
from django.template.context import Context, make_context
from django.shortcuts import render, redirect

from .apps import AportesConfig

# ==============================================================================
# URL methods
# ==============================================================================
def index(request):

    context = getContext({
    })
    return render(request, 'Aportes/index.html', context)


# ==============================================================================
# POST Only methods
# ==============================================================================
def mensal_fixo(request):
    if(request.method == 'POST'):
        capital_inicial = request['capital_inicial']
        aportes_mensais = request['aportes_mensais']
        taxa_mensal = request['taxa_mensal']
    return redirect('/aportes')


# ==============================================================================
# Utilities
# ==============================================================================
def getContext(updatedDict):
    context = dict()
    context['appName'] = AportesConfig.name
    context['pageTitle'] = AportesConfig.name

    context.update(updatedDict)
    return context
