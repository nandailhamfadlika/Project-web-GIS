from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'petaindonesia/index.html')

def welcome(request):
    return HttpResponse("<h1>Selamat Datang di Situs Kami !</h1>")
