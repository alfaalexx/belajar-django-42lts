from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'title':'Blog Bersama',
        'developer':'Udin',
        'nav':[
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }
    return render(request, 'blog/blog.html', context)

def cari(request):
    return HttpResponse('<h1>ini adalah halaman cari blog</h1>')

def artikel(request):
    context = {
        'title':'Artikel',
        'developer':'Udin'
    }
    return render(request, 'blog/blog.html', context)

def berita(request):
    context = {
        'title':'Berita',
        'developer':'Ucup'
    }
    return render(request, 'blog/blog.html', context)