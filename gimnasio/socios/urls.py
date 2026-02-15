import django
from django.urls import path
from . import views

urlpatterns = [
    # URL para la página de inicio (puede ser una vista basada en función o una vista genérica)
    path('', views.HomeView.as_view(), name='home'), 
    
    # Listas y detalles de socios
    path('socios/', views.SocioListView.as_view(), name='socio_list'),
    path('socios/<int:pk>/', views.SocioDetailView.as_view(), name='socio_detail'),
    
    # Listas y detalles de clases
    path('clases/', views.ClaseListView.as_view(), name='clase_list'),
    path('clases/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detail'),
    
    # Creación de nuevos socios (puede ser una vista basada en función o una vista genérica)
    path('socios/nuevo/', views.socio_create, name='socio_create'),  # Si usas una vista basada en función para crear socios
    
    # Actualización y eliminación de socios
    path('socios/<int:pk>/editar/', views.SocioUpdateView.as_view(), name='socio_edit'),
    path('socios/<int:pk>/eliminar/', views.SocioDeleteView.as_view(), name='socio_delete'),
]