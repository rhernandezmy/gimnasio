from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Clase, Socio

# Create your views here.
class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'
    context_object_name = 'socios'

class ClaseListView(ListView):
    model = Clase
    template_name = 'socios/clase_list.html'
    context_object_name = 'clases'
    ordering = ['horario']
    
class ClaseDetailView(DetailView):
    model = Clase
    template_name = 'socios/clase_detail.html'
    context_object_name = 'clase'
    
class SocioDetailView(DetailView):
    model = Socio
    template_name = 'socios/socio_detail.html'
    context_object_name = 'socio'