from django.shortcuts import render

# Create your views here.
from .service import get_username

def index(requests):
    context = {
        'title': get_username()
    }
    return render(requests, 'index.html', context)