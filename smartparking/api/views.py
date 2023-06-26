from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Empresa,Estacionamiento,Estado
from .serializers import(
    EmpresaSerializer,
    EstacionamientoSerializer,
    EstadoSerializer,
)
    
class EmpresaListAPIView(generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EstacionamientoListAPIView(generics.ListAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer

class EstadoListAPIView(generics.ListAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer