from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  # Asegúrate de importar el formulario
from django.views import View

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()  # Crear una instancia del formulario
        return render(request, 'registros/registro.html', {'form': form})  # Pasar el formulario al contexto
