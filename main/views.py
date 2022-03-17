from django.shortcuts import render

# Create your views here.
from .service import get_username, scrap

def index(requests):
    
    context = {
        'title': get_username(),
        'equipos': scrap()
        # 'est': prueba()
    }
    
    return render(requests, 'index.html', context)


