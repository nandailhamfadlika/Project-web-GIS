from django.shortcuts import render
from django.http import HttpResponse

def petasatu(request):
    return render(request, 'petaindonesia/petasatu.html')

def petadua(request):
    return render(request, 'petaindonesia/petadua.html')

def peta_provinsi(request):
    return render(request, "petaindonesia/peta_provinsi.html")

def petani_jawa(request):
    return render(request, "petaindonesia/petani_jawa.html")
