import json
import os

ARCHIVO = "reservas.json"

def cargar_reservas():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r") as archivo:
                return json.load(archivo)
        except:
            return []
    return []

def guardar_reservas(reservas):
    with open(ARCHIVO, "w") as archivo:
        json.dump(reservas, archivo, indent=4)