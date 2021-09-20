from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Rutas de Páginas
@app.route("/")
def get_home():
    return "Este es el home"

@app.route("/signup")
def sign_up():
    return "Este es la página de registro"


# Rutas de otras acciones
@app.route("/Producto", methods=["GET", "POST"])
def crud_producto():
    if request.method == "GET":
        # Pedir un producto
        print("Llegó un GET")
        return "Este fue un GET"

    elif request.method == "POST":
        # Registrar un producto
        request_data = request.form
        name = request_data["name"]
        brand = request_data["brand"]
        presentation = request_data["presentation"]
        category = request_data["category"]

        print("Nombre:" + name)
        print("Marca:" + brand)
        print("Presentación:" + presentation)
        print("Categoria:" + category)

        # Insertar en la base de datos el producto

        return "Se registró el producto exitosamente"



    