from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    clave = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.correo} {self.clave}" 

class Estacionamiento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    def __str__(self):
        return f"Nombre:{self.nombre} - Capacidad:{self.capacidad}" 


class Estado(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    ocupado = models.BooleanField()
    disponible = models.BooleanField()
    vehiculos_ingresados = models.IntegerField()
    def __str__(self):
        return f"{self.estacionamiento} {self.fecha}" 