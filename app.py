from flask import Flask, jsonify, request, render_template # Agregué render_template
from flask_mysqldb import MySQL

# 1. PRIMERO: Crear la aplicación
app = Flask(__name__)

# 2. SEGUNDO: Configurar la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'retail_sales_db'
mysql = MySQL(app)

# 3. TERCERO: Definir las rutas
@app.route("/")
def index():
    return render_template("insertar_producto.html")

@app.route("/api/ventas") # Cambié el nombre para que no choque con la raíz
def obtener_ventas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM ventas")
    datos = cursor.fetchall()
    cursor.close()
    return jsonify(datos)

# POST: PARA INSERTAR UNA VENTA
@app.route('/ventas', methods=['POST'])
def crear_venta():
    data = request.get_json()
    # ... (todo tu código de insertar venta)
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO ventas (fecha_venta, sucursal, cajero_id, producto, 
                                 categoria, precio_unitario, cantidad, 
                                 metodo_pago, descuento_aplicado, total_venta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (data['fecha_venta'], data['sucursal'], data['cajero_id'], 
                         data['producto'], data['categoria'], data['precio_unitario'], 
                         data['cantidad'], data['metodo_pago'], 
                         data['descuento_aplicado'], data['total_venta']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Venta registrada con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)
