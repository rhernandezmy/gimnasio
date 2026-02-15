import django
from django.urls import path
from . import views

urlpatterns = [
    # Listas y detalles de socios
    path('socios/', views.SocioListView.as_view(), name='socio_list'),
    path('socios/<int:pk>/', views.SocioDetailView.as_view(), name='socio_detail'),
    
    # Listas y detalles de clases
    path('clases/', views.ClaseListView.as_view(), name='clase_list'),
    path('clases/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detail'),
]