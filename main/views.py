from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'main/index.html', {'indx':'sdasdasdasdasdadasdadadasdads'})
def lines(request) -> HttpResponse:
    return render(request, 'main/lines.html', {'indx':'sdasdasdasdasdadasdadadasdads'})
