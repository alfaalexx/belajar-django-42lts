from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'blog/blog.html')

def cari(request):
    return HttpResponse('<h1>ini adalah halaman cari blog</h1>')