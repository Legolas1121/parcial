from flask import render_template, redirect, request, url_for
from src.config.db import createDB, installDB
from src import app
import json

@app.route('/acceso', methods=['POST'])
def setting():
    host = request.form.get('host')
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contrasena')
    servidor = request.form.get('servidor')
    puerto = request.form.get('puerto')

    dbData = {
        'host' : servidor,
        'puerto' : int(puerto),
        'usuario' : usuario,
        'contrasena' : contrasena,
        'basedatos' : host,
    }

    file = open('src/config/conexion.json', 'w')
    file.write(json.dumps(dbData))
    file.close()

    createDB()
    installDB()

    return redirect(url_for('index'))