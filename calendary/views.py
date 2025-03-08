from django.shortcuts import render
from .models import DiaDeEstudo

def lista_dias_de_estudo(request):
    dias = DiaDeEstudo.objects.all().order_by('-data')  # Ordena do mais recente para o mais antigo
    return render(request, 'dias-estudo.html', {'dias': dias})
