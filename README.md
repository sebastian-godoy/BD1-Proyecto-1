# Primer proyecto - Manual técnico
##### Sebastián Edgardo Godoy Salvatierra, 202002940
##### Lab. Bases de Datos I
#
### Funcionamiento de app
Se crea una base base de datos mediante la utilización del programa MySQL Workbench con el lenguaje MySQL, se utiliza la base de datos Proyecto1 en la dirección localhost:3306
```
DROP DATABASE Proyecto1;
create database Proyecto1;
use Proyecto1;
```
Se realizan las importaciones, se inicializa la app (API) y se invoca el modulo de MySQL Alchemy
```
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, func
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dekubaba12@localhost:3306/Proyecto1'
db = SQLAlchemy(app)
```

Se prepara la base para crear las tablas temporales y modelos temporales más adelante, aqui un ejemplo de 1 modelo y 1 tabla temporales

```
class CandidatoTemporal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.String(10))
    partido_id = db.Column(db.Integer)
    cargo_id = db.Column(db.Integer)
    
class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.String(10))
    partido_id = db.Column(db.Integer)
    cargo_id = db.Column(db.Integer)
```

Carga masiva de archivos .csv a tablas temporales parseando la informacion de manera manual

```
@app.route('/cargartabtemp',methods=['GET'])
def cargartabtemp():
    archivos_csv = [
        'candidatos.csv',
        'cargos.csv',
        'ciudadanos.csv',
        'departamentos.csv',
        'mesas.csv',
        'partidos.csv',
        'votaciones.csv',
    ]

    script_directory = os.path.dirname(__file__)  # Obtener el directorio del script Flask
    data_candidatos = []
    data_cargos = []
    data_ciudadanos = []
    data_departamentos = []
    data_mesas = []
    data_partidos = []
    data_votaciones = []
    # Crear una lista para almacenar los registros únicos de las votaciones
    registros_unicos = []
    for archivo in archivos_csv:
        ruta_absoluta = os.path.join(script_directory, archivo)  # Construir la ruta relativa
        with open(ruta_absoluta, 'r', encoding='utf-8') as csv_file:
            lines = csv_file.readlines()
            for line in lines:
                line = line.lstrip('\ufeff')
                fields = line.strip().split(',')
                if archivo == 'candidatos.csv':
                    data_candidatos.append(fields)
                elif archivo == 'cargos.csv':
                    data_cargos.append(fields)
                elif archivo == 'ciudadanos.csv':
                    data_ciudadanos.append(fields)
                elif archivo == 'departamentos.csv':
                    data_departamentos.append(fields)
                elif archivo == 'mesas.csv':
                    data_mesas.append(fields)
                elif archivo == 'partidos.csv':
                    data_partidos.append(fields)
                elif archivo == 'votaciones.csv':
                    data_votaciones.append(fields)
    i=-1
    for fila in data_candidatos:
        i+=1
        if i >=1:
            candidato_temporal = CandidatoTemporal(
                id=fila[0],
                nombres=fila[1],
                fecha_nacimiento=fila[2],
                partido_id=fila[3],
                cargo_id=fila[4],
            )
            db.session.add(candidato_temporal)
    i=-1
    for fila in data_cargos:
        i+=1
        if i >=1:
            cargo_temporal = CargoTemporal(
                id=fila[0],
                cargo=fila[1],
            )
            db.session.add(cargo_temporal)
    i=-1
    for fila in data_ciudadanos:
        i+=1
        if i >=1:
            ciudadano_temporal = CiudadanoTemporal(
                dpi=fila[0],
                Nombre=fila[1],
                Apellido=fila[2],
                Direccion=fila[3],
                Telefono=fila[4],
                Edad=fila[5],
                Genero=fila[6],
            )
            db.session.add(ciudadano_temporal)
    i=-1
    for fila in data_departamentos:
        i+=1
        if i >=1:
            departamento_temporal = DepartamentoTemporal(
                id=fila[0],
                nombre=fila[1],
            )
            db.session.add(departamento_temporal)
    i=-1
    for fila in data_mesas:
        i+=1
        if i >=1:
            mesa_temporal = MesaTemporal(
                id_mesa=fila[0],
                id_departamento=fila[1],
            )
            db.session.add(mesa_temporal)
    i=-1
    for fila in data_partidos:
        i+=1
        if i >=1:
            partido_temporal = PartidoTemporal(
                id_partido=fila[0],
                nombrePartido=fila[1],
                Siglas=fila[2],
                Fundacion=fila[3],
            )
            db.session.add(partido_temporal)
    i=-1
    for fila in data_votaciones:
        i+=1
        if i >=1:
            id_voto = fila[0]

            # Verificar si el id_voto ya existe en la lista de registros únicos
            existe_en_registros_unicos = any(registro[0] == id_voto for registro in registros_unicos)

            if not existe_en_registros_unicos:
                # Si no existe en la lista de registros únicos, agregarlo a la lista
                registros_unicos.append(fila)
            votacion_temporal = VotacionTemporal(
                id_voto=fila[0],
                id_candidato=fila[1],
                dpi_ciudadano=fila[2],
                mesa_id=fila[3],
                fecha_hora=fila[4],
            )
            db.session.add(votacion_temporal)
    for fila in registros_unicos:
        votacion = Votacion(
            id_voto=fila[0],
            id_candidato=fila[1],
            dpi_ciudadano=fila[2],
            mesa_id=fila[3],
            fecha_hora=fila[4],
        )
        db.session.add(votacion)
    db.session.commit()
    return jsonify({'message': 'Se insertaron los datos correctamente'})
```

De esta manera se crean los modelos

```
@app.route('/crearmodelo', methods=['GET'])
def crear_modelo():
    db.create_all()
    return jsonify({"message": "Tablas permanentes y modelos creados exitosamente"})
```

Aqui hay unos ejemplos de consultas

```
app.route('/consulta1', methods=['GET'])
def consulta1():
    query = text("""
    SELECT CP.nombres AS nombre_presidente, CV.nombres AS nombre_vicepresidente, P.nombrePartido AS partido
    FROM Candidato_Temporal AS CP
    JOIN Candidato_Temporal AS CV ON CP.partido_id = CV.partido_id
    JOIN Partido_Temporal AS P ON CP.partido_id = P.id_partido
    WHERE CP.cargo_id = 1 AND CV.cargo_id = 2
    """)
    result = db.session.execute(query)
    data = [{'nombre_presidente': row[0], 'nombre_vicepresidente': row[1], 'partido': row[2]} for row in result]
    return jsonify(data)

@app.route('/consulta2', methods=['GET'])
def consulta2():
    query = text("""
    SELECT P.nombrePartido AS partido, COUNT(C.id) AS num_candidatos
    FROM Candidato_Temporal AS C
    JOIN Partido_Temporal AS P ON C.partido_id = P.id_partido
    WHERE C.cargo_id IN (3, 4, 5)
    GROUP BY P.nombrePartido
    """)
    result = db.session.execute(query)
    data = [{'partido': row[0], 'num_candidatos': row[1]} for row in result]
    return jsonify(data)
```
