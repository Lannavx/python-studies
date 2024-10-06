from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    print('Home')
    return HttpResponse('Home do app atualizada')