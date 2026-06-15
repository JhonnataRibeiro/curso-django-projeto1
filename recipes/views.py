from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "recipes/home.html", context={
        "name": "Jhonnata Ribeiro"
    })

def sobre(request):
    return render(request, 'temp/temp.html')

def contato(request):
    return HttpResponse("CONTATO")