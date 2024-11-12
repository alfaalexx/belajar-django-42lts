from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'title':'Halaman Kontak',
        'developer':'Alfa Alexandra'
    }
    return render(request, 'kontak/kontak.html', context)