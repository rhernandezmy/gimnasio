from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from .forms import SocioForm, ClaseForm
from .models import Clase, Socio

# Crear un nuevo socio (vista basada en función)
def socio_create(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socio_list')  # Redirige a la lista de socios después de crear uno nuevo
    else:
        form = SocioForm()
    return render(request, 'socios/socio_create.html', {'form': form})

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
    
# Vista inicial de la web con los accesos a las diferentes secciones
class HomeView(TemplateView):
    template_name = 'socios/home.html'

def clase_create(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clase_list')  # Redirige a la lista de clases después de crear una nueva
    else:
        form = ClaseForm()
    return render(request, 'socios/clase_create.html', {'form': form})