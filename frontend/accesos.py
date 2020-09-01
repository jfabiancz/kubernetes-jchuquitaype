from flask import Flask
from datetime import datetime
import logging
import psycopg2
import sys

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

def consultas():
    conn = psycopg2.connect("host='backendapp' dbname='postgres' user='postgres' password='123456'")
    cur = conn.cursor()
    respuesta = ""

    query1 = "select count(*) from accesos;"
    dbquery = cur.execute(query1)
    conteo = cur.fetchone()
    respuesta = "Hola!  la tabla accesos tiene " + str(conteo[0])+" registro(s): </br>"
    respuesta = respuesta + "<table>"
    respuesta = respuesta + "<tr><td><b>USUARIO</b></td><td><b>EMAIL</b></td><td><b>FECHA REGISTRO</b></td></tr>"

    query2 = "select usuario,email,fecha_ini from accesos;"
    dbquery = cur.execute(query2)
    rows = cur.fetchall()
    for row in rows:
        fecha = str(row[2])
        respuesta = respuesta + "<tr><td>"+ row[0]+"</td><td>"+row[1]+"</td><td>"+fecha +"</td></tr>"
    respuesta = respuesta + "</table>"

    conn.commit()
    cur.close()
    conn.close()
    return respuesta

@app.route('/')
def cargar_accesos():
    salida = consultas()
    return salida

@app.route('/daracceso')
def daracceso():
    app.logger.debug("Se dio acceso correctamente")
    return "Se dio acceso correctamente al usuario"

