from django.urls import path
from .views import EmpresaListAPIView, EstacionamientoListAPIView, EstadoListAPIView

urlpatterns = [
    path('',EmpresaListAPIView.as_view()),
    path('empresas/', EmpresaListAPIView.as_view(), name='empresas-list'),
    path('estacionamientos/', EstacionamientoListAPIView.as_view(), name='estacionamientos-list'),
    path('estados/', EstadoListAPIView.as_view(), name='estados-list'),
]
