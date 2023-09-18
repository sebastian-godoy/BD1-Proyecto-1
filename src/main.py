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


# Consultas 1-11 ---------------------------------------------------------------------------------------------------------------
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
    query = text("""
    SELECT C.nombres AS nombre_alcalde, P.nombrePartido AS partido
    FROM Candidato AS C
    JOIN Partido AS P ON C.partido_id = P.id_partido
    WHERE C.cargo_id = 6
    """)
    result = db.session.execute(query)
    data = [{'nombre_alcalde': row[0], 'partido': row[1]} for row in result]
    return jsonify(data)

# Consulta 4: Cantidad de candidatos por partido (presidentes, vicepresidentes, diputados, alcaldes)
@app.route('/consulta4', methods=['GET'])
def consulta4():
    query = text("""
    SELECT P.nombrePartido AS partido, COUNT(C.id) AS num_candidatos
    FROM Candidato AS C
    JOIN Partido AS P ON C.partido_id = P.id_partido
    WHERE C.cargo_id IN (1, 2, 3, 4, 5, 6)
    GROUP BY P.nombrePartido
    """)
    result = db.session.execute(query)
    data = [{'partido': row[0], 'num_candidatos': row[1]} for row in result]
    return jsonify(data)

# Consulta 5: Cantidad de votaciones por departamentos
@app.route('/consulta5', methods=['GET'])
def consulta5():
    query = text("""
    SELECT D.nombre AS departamento, COUNT(V.id) AS num_votaciones
    FROM Departamento AS D
    LEFT JOIN Mesa AS M ON D.id = M.id_departamento
    LEFT JOIN Votacion AS V ON M.id_mesa = V.mesa_id
    GROUP BY D.nombre
    """)
    result = db.session.execute(query)
    data = [{'departamento': row[0], 'num_votaciones': row[1]} for row in result]
    return jsonify(data)

# Consulta 6: Cantidad de votos nulos
@app.route('/consulta6', methods=['GET'])
def consulta6():
    query = text("""
    SELECT COUNT(id) AS num_votos_nulos
    FROM Votacion
    WHERE id_candidato = -1
    """)
    result = db.session.execute(query)
    data = [{'num_votos_nulos': row[0]} for row in result]
    return jsonify(data)

# Consulta 7: Top 10 de edad de ciudadanos que realizaron su voto
@app.route('/consulta7', methods=['GET'])
def consulta7():
    query = text("""
    SELECT Edad AS edad, COUNT(*) AS cantidad
    FROM Ciudadano
    GROUP BY Edad
    ORDER BY cantidad DESC, Edad ASC
    LIMIT 10
    """)
    result = db.session.execute(query)
    data = [{'edad': row[0], 'cantidad': row[1]} for row in result]
    return jsonify(data)

# Consulta 8: Top 10 de candidatos más votados para presidente y vicepresidente (el voto por presidente incluye el vicepresidente)
@app.route('/consulta8', methods=['GET'])
def consulta8():
    query = text("""
    SELECT C.nombres AS candidato, COUNT(V.id) AS num_votos
    FROM Candidato AS C
    LEFT JOIN Votacion AS V ON C.id = V.id_candidato
    WHERE C.cargo_id IN (1, 2)
    GROUP BY C.nombres
    ORDER BY num_votos DESC
    LIMIT 10
    """)
    result = db.session.execute(query)
    data = [{'candidato': row[0], 'num_votos': row[1]} for row in result]
    return jsonify(data)

# Consulta 9: Top 5 de mesas más frecuentadas (mostrar no. Mesa y departamento al que pertenece)
@app.route('/consulta9', methods=['GET'])
def consulta9():
    query = text("""
    SELECT M.id_mesa AS no_mesa, D.nombre AS departamento, COUNT(V.id) AS num_votaciones
    FROM Mesa AS M
    LEFT JOIN Departamento AS D ON M.id_departamento = D.id
    LEFT JOIN Votacion AS V ON M.id_mesa = V.mesa_id
    GROUP BY M.id_mesa, D.nombre
    ORDER BY num_votaciones DESC
    LIMIT 5
    """)
    result = db.session.execute(query)
    data = [{'no_mesa': row[0], 'departamento': row[1], 'num_votaciones': row[2]} for row in result]
    return jsonify(data)

# Consulta 10: Mostrar el top 5 la hora más concurrida en que los ciudadanos fueron a votar
@app.route('/consulta10', methods=['GET'])
def consulta10():
    query = text("""
    SELECT SUBSTR(fecha_hora, 12, 5) AS hora, COUNT(id) AS num_votaciones
    FROM Votacion
    GROUP BY hora
    ORDER BY num_votaciones DESC
    LIMIT 5
    """)
    result = db.session.execute(query)
    data = [{'hora': row[0], 'num_votaciones': row[1]} for row in result]
    return jsonify(data)

# Consulta 11: Cantidad de votos por genero (Masculino, Femenino)
@app.route('/consulta11', methods=['GET'])
def consulta11():
    query = text("""
    SELECT Genero AS genero, COUNT(V.id) AS num_votos
    FROM Ciudadano AS C
    LEFT JOIN Votacion AS V ON C.dpi = V.dpi_ciudadano
    GROUP BY Genero
    """)
    result = db.session.execute(query)
    data = [{'genero': row[0], 'num_votos': row[1]} for row in result]
    return jsonify(data)

# Resto de consultas respecto a modelos ------------------------------------------------------
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
        INSERT INTO Departamento (id, nombre)
        SELECT DISTINCT CT.id, CT.nombre
        FROM departamento_temporal AS CT
        ON DUPLICATE KEY UPDATE id = CT.id, nombre = CT.nombre
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

        
        #db.session.commit()
        #return jsonify({"message": "Data copied to permanent tables"})

        db.session.commit()
        return jsonify({"message": "Informacion trasladada y normalizada a tablas permanentes"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/eliminartabtemp', methods=['GET'])
def eliminartabtemp():
    query = text("""
    DELETE FROM candidato_temporal;
    DELETE FROM cargo_temporal;
    DELETE FROM ciudadano_temporal;
    DELETE FROM departamento_temporal;
    DELETE FROM mesa_temporal;
    DELETE FROM partido_temporal;
    DELETE FROM votacion_temporal;
    """)
    result = db.session.execute(query)
    db.session.commit()
    return jsonify({"message": "Tablas temporales eliminadas exitosamente"})

@app.route('/eliminarmodelo', methods=['GET'])
def eliminarmodelo():
    query = text("""
    DELETE FROM candidato;
    DELETE FROM cargo;
    DELETE FROM ciudadano;
    DELETE FROM departamento;
    DELETE FROM mesa;
    DELETE FROM partido;
    DELETE FROM votacion;
    """)
    result = db.session.execute(query)
    db.session.commit()
    return jsonify({"message": "Tablas permanentes eliminadas exitosamente"})
                
# Cargar datos -------------------------------------------------------------------------------
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
    
@app.route('/crearmodelo', methods=['GET'])
def crear_modelo():
    db.create_all()
    return jsonify({"message": "Tablas permanentes y modelos creados exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)