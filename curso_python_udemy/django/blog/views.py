from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('Blog')
    return HttpResponse('Blog do app atualizada ')

def exemplo(request):
    print('Exemplo')
    return HttpResponse('Exemplo do app atualizada ')