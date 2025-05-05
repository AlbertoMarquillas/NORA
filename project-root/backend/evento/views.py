def listar_eventos(request):
    eventos = EventoRecibido.objects.order_by('-timestamp')[:50]
    datos = [
        {
            "evento": e.evento,
            "descripcion": e.descripcion,
            "tipo": e.tipo,
            "origen": e.origen,
            "timestamp": e.timestamp.isoformat(),
        }
        for e in eventos
    ]
    return JsonResponse(datos, safe=False)