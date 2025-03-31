from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import Formulario

def contacto(request):
    formulario_contacto = Formulario()

    if request.method == 'POST':
        formulario_contacto = Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

                        # Crear el mensaje que quieres enviar
            asunto = f"Nuevo mensaje de {nombre}"
            mensaje = f"Nombre: {nombre}\nEmail: {email}\n\nContenido del mensaje:\n{contenido}"
            correo_remitente = email  # El correo de la persona que envía el formulario
            destinatarios = ['tu_correo_de_prueba@gmail.com']  # Tu correo de destino

            send_mail(asunto, mensaje, correo_remitente, destinatarios)
            
            # Redirigir con el parámetro "valido" en la URL
            return redirect('contacto')  # Redirigir utilizando el nombre de la URL

    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})
