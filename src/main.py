import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, func
import csv

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




# Repite este proceso para las otras tablas temporales y permanentes

# Endpoint para cargar tablas temporales desde CSV

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
                    i=-1
                    for fila in data_candidatos:
                        if i >=0:
                            candidato_temporal = CandidatoTemporal(
                                id=fila[0],
                                nombres=fila[1],
                                fecha_nacimiento=fila[2],
                                partido_id=fila[3],
                                cargo_id=fila[4],
                            )
                            i+=1
                            db.session.add(candidato_temporal)
                elif archivo == 'cargos.csv':
                    data_cargos.append(fields)
                    i=-1
                    for fila in data_cargos:
                        if i >=0:
                            cargo_temporal = CargoTemporal(
                                id=fila[0],
                                cargo=fila[1]
                            )
                            i+=1
                            db.session.add(cargo_temporal)
                elif archivo == 'ciudadanos.csv':
                    data_ciudadanos.append(fields)
                    i=-1
                    for fila in data_ciudadanos:
                        if i >=0:
                            ciudadano_temporal = CiudadanoTemporal(
                                dpi=fila[0],
                                Nombre=fila[1],
                                Apellido=fila[2],
                                Direccion=fila[3],
                                Telefono=fila[4],
                                Edad=fila[5],
                                Genero=fila[6]
                            )
                            i+=1
                            db.session.add(ciudadano_temporal)    
                elif archivo == 'departamentos.csv':
                    data_departamentos.append(fields)
                    i=-1
                    for fila in data_departamentos:
                        if i >=0:
                            departamento_temporal = DepartamentoTemporal(
                                id_dpto=fila[0],
                                nombre=fila[1]
                            )
                            i+=1
                            db.session.add(departamento_temporal)
                elif archivo == 'mesas.csv':
                    data_mesas.append(fields)
                    i=-1
                    for fila in data_mesas:
                        if i >=0:
                            mesa_temporal = MesaTemporal(
                                id_mesa=fila[0],
                                id_departamento=fila[1]
                            )
                            i+=1
                            db.session.add(mesa_temporal)
                elif archivo == 'partidos.csv':
                    data_partidos.append(fields)
                    i=-1
                    for fila in data_partidos:
                        if i >=0:
                            partido_temporal = PartidoTemporal(
                                id_partido=fila[0],
                                nombrePartido=fila[1],
                                Siglas=fila[2],
                                Fundacion=fila[3]
                            )
                            i+=1
                            db.session.add(partido_temporal)
                elif archivo == 'votaciones.csv':
                    data_votaciones.append(fields)
                    i=-1
                    for fila in data_votaciones:
                        if i >=0:
                            votacion_temporal = VotacionTemporal(
                                id_voto=fila[0],
                                id_candidato=fila[1],
                                dpi_ciudadano=fila[2],
                                mesa_id=fila[3],
                                fecha_hora=fila[4]
                            )
                            i+=1
                            db.session.add(votacion_temporal)


    db.session.commit()
    return jsonify({"message": "Tablas temporales cargadas exitosamente"})




# Endpoint para crear tablas permanentes y modelos
@app.route('/crearmodelo', methods=['GET'])
def crear_modelo():
    db.create_all()
    return jsonify({"message": "Tablas permanentes y modelos creados exitosamente"})



# Consulta 2: Mostrar el número de candidatos a diputados por cada partido


@app.route('/consulta1', methods=['GET'])
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


@app.route('/consulta3', methods=['GET'])
def consulta3():
    query = db.session.query(
        Partido.nombrePartido.label("partido"),
        Candidato.nombres.label("nombre_alcalde")
    ).join(
        Candidato, Partido.id_partido == Candidato.partido_id
    ).filter(
        Candidato.cargo_id == 6  # Alcalde (6)
    )

    result = query.all()
    return jsonify(result)

# Consulta 4: Cantidad de candidatos por partido (presidentes, vicepresidentes, diputados, alcaldes)
@app.route('/consulta4', methods=['GET'])
def consulta4():
    query = db.session.query(
        Partido.nombrePartido.label("partido"),
        func.count(Candidato.id).label("num_candidatos")
    ).join(
        Candidato, Partido.id_partido == Candidato.partido_id
    ).group_by(Partido.nombrePartido)

    result = query.all()
    return jsonify(result)

# Consulta 5: Cantidad de votaciones por departamentos
@app.route('/consulta5', methods=['GET'])
def consulta5():
    query = db.session.query(
        Departamento.nombre.label("departamento"),
        func.count(Votacion.id_voto).label("num_votaciones")
    ).join(
        Mesa, Departamento.id == Mesa.id_departamento
    ).join(
        Votacion, Mesa.id_mesa == Votacion.mesa_id
    ).group_by(Departamento.nombre)

    result = query.all()
    return jsonify(result)

# Consulta 6: Cantidad de votos nulos
@app.route('/consulta6', methods=['GET'])
def consulta6():
    query = db.session.query(
        func.count(Votacion.id_voto).label("num_votos_nulos")
    ).filter(
        Votacion.id_candidato == -1  # Considerar votos con id_candidato igual a -1 como nulos
    )

    result = query.scalar()
    return jsonify({"num_votos_nulos": result})

# Consulta 7: Top 10 de edad de ciudadanos que realizaron su voto
@app.route('/consulta7', methods=['GET'])
def consulta7():
    query = db.session.query(
        Ciudadano.Edad.label("edad")
    ).order_by(
        Ciudadano.Edad
    ).limit(10)

    result = query.all()
    return jsonify(result)

# Consulta 8: Top 10 de candidatos más votados para presidente y vicepresidente (el voto por presidente incluye el vicepresidente)
@app.route('/consulta8', methods=['GET'])
def consulta8():
    query = db.session.query(
        Candidato.nombres.label("candidato"),
        func.count(Votacion.id_voto).label("num_votos")
    ).filter(
        Candidato.cargo_id.in_([1, 2])  # Presidente (1) o Vicepresidente (2)
    ).group_by(
        Candidato.nombres
    ).order_by(
        func.count(Votacion.id_voto).desc()
    ).limit(10)

    result = query.all()
    return jsonify(result)

# Consulta 9: Top 5 de mesas más frecuentadas (mostrar no. Mesa y departamento al que pertenece)
@app.route('/consulta9', methods=['GET'])
def consulta9():
    query = db.session.query(
        Mesa.id_mesa.label("no_mesa"),
        Departamento.nombre.label("departamento"),
        func.count(Votacion.id_voto).label("num_votaciones")
    ).join(
        Departamento, Mesa.id_departamento == Departamento.id
    ).join(
        Votacion, Mesa.id_mesa == Votacion.mesa_id
    ).group_by(
        Mesa.id_mesa
    ).order_by(
        func.count(Votacion.id_voto).desc()
    ).limit(5)

    result = query.all()
    return jsonify(result)

# Consulta 10: Mostrar el top 5 la hora más concurrida en que los ciudadanos fueron a votar
@app.route('/consulta10', methods=['GET'])
def consulta10():
    query = db.session.query(
        func.substr(Votacion.fecha_hora, 12, 5).label("hora"),
        func.count(Votacion.id_voto).label("num_votaciones")
    ).group_by(
        func.substr(Votacion.fecha_hora, 12, 5)
    ).order_by(
        func.count(Votacion.id_voto).desc()
    ).limit(5)

    result = query.all()
    return jsonify(result)

# Consulta 11: Cantidad de votos por genero (Masculino, Femenino)
@app.route('/consulta11', methods=['GET'])
def consulta11():
    query = db.session.query(
        Ciudadano.Genero.label("genero"),
        func.count(Votacion.id_voto).label("num_votos")
    ).join(
        Votacion, Ciudadano.dpi == Votacion.dpi_ciudadano
    ).group_by(
        Ciudadano.Genero
    )
    result = query.all()
    return jsonify(result)

# Consulta 3: Mostrar el nombre de los candidatos a alcalde por partido
@app.route('/cargarmodelo', methods=['GET'])
def cargar_modelo():
    try:
        # Copy data from CandidatoTemporal to permanent Candidato table
        query = text("""
        INSERT INTO Candidato (nombres, fecha_nacimiento, partido_id, cargo_id)
        SELECT DISTINCT CT.nombres, CT.fecha_nacimiento, CT.partido_id, CT.cargo_id
        FROM candidato_temporal AS CT
        ON DUPLICATE KEY UPDATE
        nombres = CT.nombres, fecha_nacimiento = CT.fecha_nacimiento,
        partido_id = CT.partido_id, cargo_id = CT.cargo_id
        """)
        db.session.execute(query)

        # Copy data from CargoTemporal to permanent Cargo table
        query = text("""
        INSERT INTO Cargo (cargo)
        SELECT DISTINCT CT.cargo
        FROM cargo_temporal AS CT
        ON DUPLICATE KEY UPDATE cargo = CT.cargo
        """)
        db.session.execute(query)

        # Copy data from CiudadanoTemporal to permanent Ciudadano table
        query = text("""
        INSERT INTO Ciudadano (dpi, Nombre, Apellido, Direccion, Telefono, Edad, Genero)
        SELECT DISTINCT CT.dpi, CT.Nombre, CT.Apellido, CT.Direccion, CT.Telefono, CT.Edad, CT.Genero
        FROM ciudadano_temporal AS CT
        ON DUPLICATE KEY UPDATE
        Nombre = CT.Nombre, Apellido = CT.Apellido,
        Direccion = CT.Direccion, Telefono = CT.Telefono,
        Edad = CT.Edad, Genero = CT.Genero
        """)
        db.session.execute(query)

        # Copy data from DepartamentoTemporal to permanent Departamento table
        query = text("""
        INSERT INTO Departamento (id_dpto, nombre)
        SELECT DISTINCT CT.id_dpto, CT.nombre
        FROM departamento_temporal AS CT
        ON DUPLICATE KEY UPDATE id_dpto = CT.id_dpto, nombre = CT.nombre
        """)
        db.session.execute(query)

        # Copy data from MesaTemporal to permanent Mesa table
        query = text("""
        INSERT INTO Mesa (id_mesa, id_departamento)
        SELECT DISTINCT CT.id_mesa, CT.id_departamento
        FROM mesa_temporal AS CT
        ON DUPLICATE KEY UPDATE id_mesa = CT.id_mesa, id_departamento = CT.id_departamento
        """)
        db.session.execute(query)

        # Copy data from PartidoTemporal to permanent Partido table
        query = text("""
        INSERT INTO Partido (id_partido, nombrePartido, Siglas, Fundacion)
        SELECT DISTINCT CT.id_partido, CT.nombrePartido, CT.Siglas, CT.Fundacion
        FROM partido_temporal AS CT
        ON DUPLICATE KEY UPDATE
        nombrePartido = CT.nombrePartido, Siglas = CT.Siglas, Fundacion = CT.Fundacion
        """)
        db.session.execute(query)

        # Copy data from VotacionTemporal to permanent Votacion table
        query = text("""
        INSERT INTO Votacion (id_voto, id_candidato, dpi_ciudadano, mesa_id, fecha_hora)
        SELECT DISTINCT CT.id_voto, CT.id_candidato, CT.dpi_ciudadano, CT.mesa_id, CT.fecha_hora
        FROM votacion_temporal AS CT
        ON DUPLICATE KEY UPDATE
        id_candidato = CT.id_candidato, dpi_ciudadano = CT.dpi_ciudadano,
        mesa_id = CT.mesa_id, fecha_hora = CT.fecha_hora
        """)
        db.session.execute(query)

        db.session.commit()
        return jsonify({"message": "Data copied to permanent tables"})
    except Exception as e:
        return jsonify({"error": str(e)})


    

if __name__ == '__main__':
    app.run(debug=True)