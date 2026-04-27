from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# --- 1. CONFIGURACIÓN DE LA BASE DE DATOS ---
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # En XAMPP suele estar vacío
app.config['MYSQL_DB'] = 'retail_sales_db'

# --- 2. INICIALIZAR LA CONEXIÓN ---
mysql = MySQL(app)

@app.route("/")
def obtener_ventas():
    # --- 3. PROCESO DE CONSULTA ---
    # Creamos un cursor (el mensajero que va a la base de datos)
    cur = mysql.connection.cursor()
    
    # Le damos la orden SQL que ya conoces
    cur.execute("SELECT * FROM ventas")
    
    # Traemos todos los resultados
    datos = cur.fetchall()
    
    # Cerramos el mensajero para liberar memoria
    cur.close()
    
    # Por ahora, solo devolvemos los datos crudos para ver si conectó
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)