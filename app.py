from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)