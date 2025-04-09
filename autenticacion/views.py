from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Asegúrate de importar AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views import View

# Vista para el registro de usuario
class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()  # Crear una instancia del formulario
        return render(request, 'registros/registro.html', {'form': form})  # Pasar el formulario al contexto
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save() 
            login(request, usuario)  # Iniciar sesión al usuario después del registro exitoso
            return redirect('home')  # Redirigir a la página de inicio después del registro exitoso
        else:
            # Si el formulario no es válido, renderiza de nuevo con los errores
            return render(request, 'registros/registro.html', {'form': form})  # Muestra el formulario con los errores


# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)  # Cerrar sesión
    return redirect('home')  # Redirigir a la página de inicio


# Vista para iniciar sesión (logear)
def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, autenticar al usuario
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')  # Redirigir a la página de inicio
        else:
            return render(request, 'login/loger.html', {'form': form})  # Mostrar los errores del formulario
    else:
        form = AuthenticationForm()  # Crear un formulario vacío para el GET
        return render(request, 'login/loger.html', {'form': form})  # Renderizar la plantilla con el formulario
