from django.shortcuts import render

# Create your views here.
from .service import get_username, scrap, resultados

def index(requests):
    
    context = {
        'title': get_username(),
        'equipos': scrap(),
        'resultados': resultados()
    }
    
    return render(requests, 'index.html', context)


