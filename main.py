from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """
    Página inicial con el menú principal.
    Contiene botones para ir a Ejercicio 1 y Ejercicio 2.
    """
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    """
    Formulario:
      - nombre
      - edad
      - cantidad de tarros de pintura

    Precio por tarro: 9000

    Descuentos:
      - edad < 18                  -> 0%
      - 18 <= edad <= 30           -> 15%
      - edad > 30                  -> 25%
    """
    resultado = None
    error = None

    if request.method == "POST":
        try:
            nombre = request.form.get("nombre", "").strip()
            edad = int(request.form.get("edad", "0"))
            tarros = int(request.form.get("tarros", "0"))

            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if edad <= 0:
                raise ValueError("La edad debe ser un número positivo.")
            if tarros <= 0:
                raise ValueError("La cantidad de tarros debe ser positiva.")

            precio_por_tarro = 9000
            total_sin_descuento = tarros * precio_por_tarro

            # Cálculo de descuento según edad
            if edad < 18:
                porcentaje_descuento = 0
            elif 18 <= edad <= 30:
                porcentaje_descuento = 15
            else:  # edad > 30
                porcentaje_descuento = 25

            monto_descuento = total_sin_descuento * (porcentaje_descuento / 100)
            total_con_descuento = total_sin_descuento - monto_descuento

            resultado = {
                "nombre": nombre,
                "edad": edad,
                "tarros": tarros,
                "total_sin_descuento": total_sin_descuento,
                "porcentaje_descuento": porcentaje_descuento,
                "total_con_descuento": total_con_descuento,
            }

        except ValueError as e:
            error = str(e)

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    """
    Login simple con dos usuarios:
      - juan / admin -> "Bienvenido administrador juan"
      - pepe / user  -> "Bienvenido usuario pepe"
      - cualquier otro -> "Usuario o contraseña incorrectos"
    """
    mensaje = None

    # Usuarios hardcodeados
    usuarios = {
        "juan": {"password": "admin", "tipo": "administrador"},
        "pepe": {"password": "user", "tipo": "usuario"},
    }

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "").strip()

        if usuario in usuarios and usuarios[usuario]["password"] == password:
            tipo = usuarios[usuario]["tipo"]
            mensaje = f"Bienvenido {tipo} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    # Ejecutar la aplicación en modo debug para desarrollo
    app.run(debug=True)
