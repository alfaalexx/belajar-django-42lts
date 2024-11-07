#kode dibawah ini seharusnya berada di file views.py
from django.http import HttpResponse

#django menyediakan package jalan pintas 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
