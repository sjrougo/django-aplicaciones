from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def endpoint1_e_commerce(request):
    print('Ingresó a e-commerce')
    return HttpResponse('<h1>Ingresó a e-commerce</h1>')


def endpoint2_e_commerce(request):
    print('Ingresó a la segunda página e-commerce')
    return HttpResponse('<h1>Ingresó a la segunda página e-commerce</h1>')
