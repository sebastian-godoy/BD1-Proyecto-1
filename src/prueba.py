import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, func
import csv

#db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dekubaba12@localhost:3306/Proyecto1'
db = SQLAlchemy(app)
# Candidato -----------------------------------
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

# Cargo -----------------------------------
class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(255))

class CargoTemporal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(255))

# Ciudadano -----------------------------------
class Ciudadano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dpi = db.Column(db.String(255))
    Nombre = db.Column(db.String(255))
    Apellido = db.Column(db.String(255))
    Direccion = db.Column(db.String(255))
    Telefono = db.Column(db.String(30))
    Edad = db.Column(db.Integer)
    Genero = db.Column(db.String(1))

class CiudadanoTemporal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dpi = db.Column(db.String(255))
    Nombre = db.Column(db.String(255))
    Apellido = db.Column(db.String(255))
    Direccion = db.Column(db.String(255))
    Telefono = db.Column(db.String(30))
    Edad = db.Column(db.Integer)
    Genero = db.Column(db.String(1))

# Departamento -----------------------------------
class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #id_dpto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
class DepartamentoTemporal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #id_dpto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))

# Mesa -----------------------------------
class Mesa(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id_mesa = db.Column(db.Integer, primary_key=True)
    id_departamento = db.Column(db.Integer)
class MesaTemporal(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id_mesa = db.Column(db.Integer, primary_key=True)
    id_departamento = db.Column(db.Integer)

# Partido -----------------------------------
class Partido(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id_partido = db.Column(db.Integer, primary_key=True)
    nombrePartido = db.Column(db.String(255))
    Siglas = db.Column(db.String(255))
    Fundacion = db.Column(db.String(10))
class PartidoTemporal(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id_partido = db.Column(db.Integer, primary_key=True)
    nombrePartido = db.Column(db.String(255))
    Siglas = db.Column(db.String(255))
    Fundacion = db.Column(db.String(10))

# Votacion -----------------------------------
class Votacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_voto = db.Column(db.Integer)
    id_candidato = db.Column(db.Integer)
    dpi_ciudadano = db.Column(db.String(40))
    mesa_id = db.Column(db.Integer)
    fecha_hora = db.Column(db.String(30))
class VotacionTemporal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_voto = db.Column(db.Integer)
    id_candidato = db.Column(db.Integer)
    dpi_ciudadano = db.Column(db.String(40))
    mesa_id = db.Column(db.Integer)
    fecha_hora = db.Column(db.String(30))

@app.route('/consultaPrueba1',methods=['GET'])
def consultaPrueba1():
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

    for archivo in archivos_csv:
        ruta_absoluta = os.path.join(script_directory, archivo)  # Construir la ruta relativa
        with open(ruta_absoluta, 'r', encoding='utf-8') as csv_file:
            #csv_reader = csv.DictReader(csv_file)
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
            votacion_temporal = VotacionTemporal(
                id_voto=fila[0],
                id_candidato=fila[1],
                dpi_ciudadano=fila[2],
                mesa_id=fila[3],
                fecha_hora=fila[4],
            )
            db.session.add(votacion_temporal)
    
   
    db.session.commit()
    return jsonify({'message': 'Se insertaron los datos correctamente'})


# Endpoint para crear tablas permanentes y modelos
@app.route('/crearmodelo', methods=['GET'])
def crear_modelo():
    db.create_all()
    return jsonify({"message": "Tablas permanentes y modelos creados exitosamente"})

    

if __name__ == '__main__':
    app.run(debug=True)