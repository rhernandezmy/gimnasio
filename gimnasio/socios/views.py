from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from gimnasio.socios.form import SocioForm
from .models import Clase, Socio

# Lista de socios
class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'
    context_object_name = 'socios'
# Detalle de un socio
class SocioDetailView(DetailView):
    model = Socio
    template_name = 'socios/socio_detail.html'
    context_object_name = 'socio'
    
# Lista de clases
class ClaseListView(ListView):
    model = Clase
    template_name = 'socios/clase_list.html'
    context_object_name = 'clases'
    ordering = ['horario']

# Detalle de una clase    
class ClaseDetailView(DetailView):
    model = Clase
    template_name = 'socios/clase_detail.html'
    context_object_name = 'clase'
    
# Vista para actualizar los datos de un socio
class SocioUpdateView(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socio_list')
    
# Vista para eliminar un socio
class SocioDeleteView(DeleteView):
    model = Socio
    template_name = 'socios/socio_confirm_delete.html'
    success_url = reverse_lazy('socio_list')