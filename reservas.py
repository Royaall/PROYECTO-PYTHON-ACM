# CONFIGURACIÓN
TOTAL_MESAS = 5
CAPACIDAD_MESA = 70
HORARIOS = ["18:00", "19:00", "20:00", "21:00"]

# ------------------------------

def mostrar_reservas(reservas):
    if not reservas:
        print("No hay reservas agendadas.")
    else:
        for r in reservas:
            print("ID:", r["id"])
            print("Nombre:", r["nombre"])
            print("Personas:", r["personas"])
            print("Hora:", r["hora"])
            print("Mesa:", r["mesa"])
            print("-------------------------")

# ------------------------------

def obtener_mesa_disponible(reservas, hora):
    ocupadas = []

    for r in reservas:
        if r["hora"] == hora:
            ocupadas.append(r["mesa"])

    for mesa in range(1, TOTAL_MESAS + 1):
        if mesa not in ocupadas:
            return mesa

    return None

# ------------------------------

def crear_reserva(reservas, nombre, personas, hora):

    if personas > CAPACIDAD_MESA:
        print("No se puede: supera la capacidad de la mesa.")
        return

    mesa = obtener_mesa_disponible(reservas, hora)

    if mesa is None:
        print("No hay mesas disponibles en ese horario.")
        return

    if reservas:
        nuevo_id = max(r["id"] for r in reservas) + 1
    else:
        nuevo_id = 1

    reserva = {
        "id": nuevo_id,
        "nombre": nombre,
        "personas": personas,
        "hora": hora,
        "mesa": mesa
    }

    reservas.append(reserva)
    print(f"Reserva creada. Mesa asignada: {mesa}")

# ------------------------------

def buscar_reserva(reservas, id_buscar):
    for r in reservas:
        if r["id"] == id_buscar:
            return r
    return None

# ------------------------------

def modificar_reserva(reserva, id, nombre, personas):

    
    nuevo = nombre
    reserva["nombre"] = nuevo


    nuevo_personas = personas
    if nuevo_personas > CAPACIDAD_MESA:
        return
    reserva["personas"] = nuevo_personas

# ------------------------------

def eliminar_reserva(reservas, id):
    id_buscar = int(id)
    reserva = buscar_reserva(reservas, id_buscar)

    if reserva is None:
        print("No se encontró la reserva.")
        return 

    reservas.remove(reserva)