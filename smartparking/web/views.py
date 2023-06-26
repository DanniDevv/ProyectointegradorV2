from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Empresa, Estacionamiento, Estado
from django.contrib import messages



from django.contrib.auth.decorators import login_required

def lista_estacionamientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request, 'index-home.html', {'estacionamientos': estacionamientos})

def estados_estacionamiento(request, estacionamiento_id):
    estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
    estados = Estado.objects.filter(estacionamiento=estacionamiento)
    return render(request, 'estados_estacionamiento.html', {'estacionamiento': estacionamiento, 'estados': estados})

def empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})



def login(request):
    if request.method == 'POST':
        correo = request.POST['username']
        clave = request.POST['password']

        try:
            empresa = Empresa.objects.get(correo=correo)
            if empresa.clave == clave:
                # Las credenciales son correctas, realizar alguna acción (por ejemplo, redirigir a otra página)
                return render(request, 'index-aboutO.html')
            else:
                # La clave es incorrecta, mostrar un mensaje de error
                messages.error(request, 'La clave ingresada es incorrecta.')
        except Empresa.DoesNotExist:
            # No se encontró ninguna empresa con el correo ingresado, mostrar un mensaje de error
            messages.error(request, 'No existe una cuenta asociada a ese correo.')

    return render(request, 'login.html')

def principal(request):
    return render(request, 'index-principal.html')
def home(request):
    return render(request, 'index-home.html')