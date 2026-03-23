# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Henze Fernandes em SO!")

