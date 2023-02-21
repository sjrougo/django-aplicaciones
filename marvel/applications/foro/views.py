from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def endpoint1_foro(request):
    print('Ingresó al foro')
    return HttpResponse('<h1>Ingresó al foro</h1>')
