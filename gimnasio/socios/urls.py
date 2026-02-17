import django
from django.urls import path
from . import views

urlpatterns = [
    # URL para la página de inicio 
    path('', views.HomeView.as_view(), name='home'), 
    
    # Listas y detalles de socios
    path('socios/', views.SocioListView.as_view(), name='socio_list'),
    path('socios/<int:pk>/', views.SocioDetailView.as_view(), name='socio_detail'),
    
    # Listas y detalles de clases
    path('clases/', views.ClaseListView.as_view(), name='clase_list'),
    path('clases/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detail'),
    
    # Listas y detalles de entrenadores
    path('entrenadores/', views.EntrenadorListView.as_view(), name='entrenador_list'),
    path('entrenadores/<int:pk>/', views.EntrenadorDetailView.as_view(), name='entrenador_detail'),
    
    # Creación de nuevos socios 
    path('socios/nuevo/', views.socio_create, name='socio_create'),  
    
    # Creación de nuevos entrenadores
    path('entrenadores/nuevo/', views.entrenador_create, name='entrenador_create'), 
    
    # Actualización y eliminación de socios
    path('socios/<int:pk>/editar/', views.SocioUpdateView.as_view(), name='socio_update'),
    path('socios/<int:pk>/eliminar/', views.SocioDeleteView.as_view(), name='socio_delete'),
    
     # Creación de nuevas clases 
    path('clases/nuevo/', views.clase_create, name='clase_create'),
]