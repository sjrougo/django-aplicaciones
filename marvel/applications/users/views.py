from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def endpoint1_users(request):
    print('Ingresó a usuarios')
    return HttpResponse('<h1>Ingresó a usuarios</h1>')
