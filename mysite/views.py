#kode dibawah ini seharusnya berada di file views.py
from django.http import HttpResponse

#django menyediakan package jalan pintas 
from django.shortcuts import render

def index(request):
    context = {
        'title':'Web Development',
        'developer':'Alfa Alexandra Simanjuntak',
        'banner':'static/images/beranda.png'
    }
    return render(request, 'index.html', context)
