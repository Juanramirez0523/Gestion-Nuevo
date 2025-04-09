def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            # Calcula el total solo si el carro existe en la sesión
            for key, value in request.session["carro"].items():
                total += float(value["precio"])  # Sumar el precio de cada producto en el carro
        else:
            # Si no hay productos en el carro
            total = 0
    else:
        # Si el usuario no está autenticado, muestra un mensaje o 0
        total = "Haz Login"

    return {"importe_total_carro": total}
