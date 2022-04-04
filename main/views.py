from django.shortcuts import render

# Create your views here.
from .service import get_username, tabla, resultados, goles, tarjetas, calendario, tablaLibertadores

def index(requests):
    
    context = {
        'title': get_username(),
        #'equipos': scrap(),
        'resultados': resultados(),
        'tabla': tabla(),
        'goles': goles(),
        'tarjetas': tarjetas(),
        'calendario': calendario(),
        'tablaLibertadores': tablaLibertadores()
    }
    
    return render(requests, 'index.html', context)


