from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'retail_sales_db'
mysql = MySQL(app)

@app.route("/")
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
    fecha_venta = data['fecha_venta']
    sucursal = data['sucursal']
    cajero_id = data['cajero_id']
    producto = data['producto']
    categoria = data['categoria']
    precio_unitario = data['precio_unitario']
    cantidad = data['cantidad']
    metodo_pago = data['metodo_pago']
    descuento_aplicado = data['descuento_aplicado']
    total_venta = data['total_venta']
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO ventas (fecha_venta, sucursal, cajero_id, producto, 
                                 categoria, precio_unitario, cantidad, 
                                 metodo_pago, descuento_aplicado, total_venta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (fecha_venta, sucursal, cajero_id, producto, 
                         categoria, precio_unitario, cantidad, 
                         metodo_pago, descuento_aplicado, total_venta))
    
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"mensaje": "Venta registrada con éxito"}), 201


if __name__ == '__main__':
    app.run(debug=True)