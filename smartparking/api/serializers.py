from rest_framework import serializers
from web.models import Empresa, Estacionamiento, Estado

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'correo', 'clave']

class EstacionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamiento
        fields = ['id', 'empresa', 'nombre', 'direccion', 'capacidad']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'estacionamiento', 'fecha', 'ocupado', 'disponible', 'vehiculos_ingresados']
