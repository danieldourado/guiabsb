from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import string



def checkIfThereIsString(model, slug):
    objects = model.objects.all()
    for obj in objects:
        if obj.slug in slug:
            return obj.slug + ' é do tipo ' + obj.__class__.__name__ + '; <br/>'
    return ''

# Create your views here.
def detail(request, slug):
    name = ''
    name += checkIfThereIsString(Cidade,slug)
    name += checkIfThereIsString(Transacao,slug)
    name += checkIfThereIsString(Tipo,slug)
    name += checkIfThereIsString(Quarto,slug)
    name += checkIfThereIsString(Banheiro,slug)
    name += checkIfThereIsString(Vaga,slug)
    name += checkIfThereIsString(Anuncio,slug)
    


    return HttpResponse(name)

