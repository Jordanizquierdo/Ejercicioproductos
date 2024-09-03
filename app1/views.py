from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hola(request):
    return HttpResponse("<h1>HOLA<h1>")

def pag(request):
    data = {"nombre":"Jordan"}
    return render(request,'app1/index.html',data)