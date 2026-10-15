from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ.get("AURABEAUTY_SECRET_KEY", "cambia-esta-clave-en-produccion")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_FILE = os.path.join(BASE_DIR, "contactos.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    tema = request.form.get("tema", "").strip()
    mensaje = request.form.get("mensaje", "").strip()
    consentimiento = request.form.get("consentimiento")

    if not nombre or not correo or not mensaje or not consentimiento:
        flash("Completa los campos obligatorios y acepta el aviso de privacidad.", "danger")
        return redirect(url_for("index") + "#contacto")

    # Este prototipo guarda los mensajes localmente. No lo publiques con datos reales
    # sin implementar controles de seguridad, acceso, retención y tratamiento de datos.
    existe = os.path.exists(CONTACTS_FILE)
    with open(CONTACTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["fecha", "nombre", "correo", "tema", "mensaje"])
        writer.writerow([datetime.now().isoformat(timespec="seconds"), nombre, correo, tema, mensaje])

    flash("Mensaje guardado en el prototipo. Gracias por contactar a AURABEAUTY.", "success")
    return redirect(url_for("index") + "#contacto")

if __name__ == "__main__":
    # Ejecutar solo en entorno de desarrollo: python app.py
    app.run(debug=True)
