from app import db

# Tabla Producto
class Product(db.Model):
    __tablename__ = 'Product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    presentation = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    due_date = db.Column(db.Date, nullable=True)
    income_type = db.Column(db.String)
    supplier = db.Column(db.String)
    location = db.Column(db.String)

    # insertar constructor tabla producto
    def __init__(self,name,brand,presentation,category,price,amount,due_date,income_type,supplier,location):
        self.name = name
        self.brand = brand
        self.presentation = presentation
        self.category = category
        self.price = price
        self.amount = amount
        self.due_date = due_date
        self.income_type = income_type
        self.supplier = supplier
        self.location = location

# Tabla Administrador

class Administrator(db.Model):
    __tablename__ = 'Administrator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

# Tabla Factura de Venta

class Invoice(db.Model):
    __tablename__ = 'Invoice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Integer)
    unit_value = db.Column(db.Integer)
    total_value = db.Column(db.Integer)