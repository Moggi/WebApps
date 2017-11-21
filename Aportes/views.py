from django.http import HttpResponse
from django.template.context import Context, make_context
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
def mensal(request):
    if(request.method == 'POST'):
        capital_inicial = float(request.POST['capital_inicial'])
        aportes_mensais = float(request.POST['aportes_mensais'])
        taxa_mensal     = float(request.POST['taxa_mensal'])
        taxa_progressiva = float(request.POST['taxa_progressiva'])

        taxa_mensal     = (taxa_mensal/100) if taxa_mensal >= 0 else 1

        capital_investido = capital_inicial

        valor_anual = capital_inicial

        valores_mensais = []

        it = 100 # 100 anos
        for it in range(1, 100 +1):

            valor_mensal = valor_anual
            for mes in range(1, 12 +1):
                capital_investido += aportes_mensais
                valor_mensal = (valor_mensal+aportes_mensais)*(1+taxa_mensal)

            valor_anual = valor_mensal

            valores_mensais.append({
                'aportes_mensais': aportes_mensais,
                'capital_investido': capital_investido,
                'valor_anual': valor_anual,
                'lucro_anual': valor_anual-capital_investido,
                'lucro_anual_15': (valor_anual-capital_investido)*0.85,
                'lucro_anual_175': (valor_anual-capital_investido)*0.825,
                'lucro_anual_20': (valor_anual-capital_investido)*0.80,
                'lucro_anual_225': (valor_anual-capital_investido)*0.775,
            })

            if (valor_anual-capital_investido)*(0.775)/1000000 >= 1:
                break

            if taxa_progressiva > 0.0001:
                aportes_mensais += aportes_mensais*taxa_progressiva

        context = getContext({
            'capital_inicial': capital_inicial,
            'taxa_mensal': taxa_mensal,
            'valores_mensais': valores_mensais,
        })
        return render(request, 'Aportes/mensal.html', context)
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
