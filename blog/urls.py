from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('cari/',views.cari),
    path('artikel/', views.artikel),
    path('berita/', views.berita)
]