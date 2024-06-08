from django.shortcuts import render

from .models import *

def home(request):
    paises = Country.objects.all()
    anuncios = Anuncio.objects.all()
    return render(request, 'lcdhsite/home.html', {'logo': 'images/logo.webp', 'paises': paises, 'anuncios': anuncios})
