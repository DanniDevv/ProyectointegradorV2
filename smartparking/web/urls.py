from django.urls import path
from . import views 

app_name = 'smartparking'  # Reemplaza "nombre_de_tu_aplicacion" con el nombre real de tu aplicación

urlpatterns = [
    path('', views.lista_estacionamientos, name='estacionamientos'),
    path('estados_estacionamiento/<int:estacionamiento_id>/', views.estados_estacionamiento, name='estados_estacionamiento'),
    path('empresas/', views.empresas, name='empresas'),
    path('login/',views.login, name="login"),

    path('principal/',views.principal, name='principal'),
    path('home/',views.home, name='home')
]