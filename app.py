from flask import Flask, render_template, request, redirect, url_for

from persistencia import cargar_reservas, guardar_reservas
from reservas import crear_reserva, modificar_reserva, eliminar_reserva, buscar_reserva

app = Flask(__name__)


# 🏠 HOME
@app.route("/")
def index():
    reservas = cargar_reservas()
    return render_template("index.html", reservas=reservas)

@app.route("/ver")
def ver():
    reservas = cargar_reservas()
    return render_template("ver.html", reservas=reservas)


# ➕ CREAR 
@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        personas = int(request.form["personas"])
        hora = request.form["hora"]
        

        reservas = cargar_reservas()

        crear_reserva(reservas, nombre, personas, hora)
        guardar_reservas(reservas)

        cambio = True
        
        return render_template("crear.html", cambio=cambio)

    return render_template("crear.html")


# ✏️ EDITAR
@app.route("/editar", methods=["GET", "POST"])
def editar():
    reservas = cargar_reservas()
    if request.method == "POST":
        id = int(request.form["id"])
        reserva = buscar_reserva(reservas, id)
        
        return render_template("editar.html", reserva=reserva)
    

    return render_template("editar.html", reserva=None)

@app.route("/editar_guardar", methods=["GET", "POST"])
def editar_guardar():
    reservas = cargar_reservas()
    if request.method == "POST":
        id = int(request.form["id"])
        nombre = request.form["nombre"]
        personas =  int(request.form["personas"])
        reserva = buscar_reserva(reservas, id)
        modificar_reserva(reserva, id, nombre, personas)
        guardar_reservas(reservas)
        
        cambio = True
        
        return render_template("editar.html", cambio=cambio)
    return render_template("editar.html", reserva=None)

# ❌ ELIMINAR
@app.route("/eliminar", methods=["GET", "POST"])
def eliminar(): 
    
    reservas = cargar_reservas()
    if request.method == "POST":
        id = int(request.form["id"])
        reserva = buscar_reserva(reservas, id)
        
        return render_template("eliminar.html", reserva=reserva)
        

        

    return render_template("eliminar.html", reserva=None)

@app.route("/eliminar_guardar", methods=["GET", "POST"])
def eliminar_guardar():
    reservas = cargar_reservas()
    if request.method == "POST":
        id = int(request.form["id"])
        eliminar_reserva(reservas, id)
        guardar_reservas(reservas)
        
        cambio = True
        
        return render_template("editar.html", cambio=cambio)
    return render_template("eliminar.html", reservas=None)


# 🚀 RUN
if __name__ == "__main__":
    app.run(debug=True)