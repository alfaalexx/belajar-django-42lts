#kode dibawah ini seharusnya berada di file views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def blog(request):
    return HttpResponse("Halaman Blog")