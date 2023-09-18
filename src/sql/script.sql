# Borrar y crear base de datos
DROP DATABASE Proyecto1;
create database Proyecto1;
use Proyecto1;

# Ver tablas
show tables from Proyecto1;
SELECT * FROM candidato_temporal;
SELECT * FROM cargo_temporal;
SELECT * FROM ciudadano_temporal;
SELECT * FROM departamento_temporal;
SELECT * FROM mesa_temporal;
SELECT * FROM votacion_temporal;
SELECT * FROM candidato;
SELECT * FROM cargo;
SELECT * FROM ciudadano;
SELECT * FROM departamento;
SELECT * FROM mesa;
SELECT * FROM votacion;

# Consulta 1
SELECT CP.nombres AS nombre_presidente, CV.nombres AS nombre_vicepresidente, P.nombrePartido AS partido
FROM Candidato_Temporal AS CP
JOIN Candidato_Temporal AS CV ON CP.partido_id = CV.partido_id
JOIN Partido_Temporal AS P ON CP.partido_id = P.id_partido
WHERE CP.cargo_id = 1 AND CV.cargo_id = 2;

# Consulta 2
SELECT P.nombrePartido AS partido, COUNT(C.id) AS num_candidatos
FROM Candidato_Temporal AS C
JOIN Partido_Temporal AS P ON C.partido_id = P.id_partido
WHERE C.cargo_id IN (3, 4, 5)
GROUP BY P.nombrePartido;

# Consulta 3
SELECT C.nombres AS nombre_alcalde, P.nombrePartido AS partido
FROM Candidato AS C
JOIN Partido AS P ON C.partido_id = P.id_partido
WHERE C.cargo_id = 6;

# Consulta 4
SELECT P.nombrePartido AS partido, COUNT(C.id) AS num_candidatos
FROM Candidato AS C
JOIN Partido AS P ON C.partido_id = P.id_partido
WHERE C.cargo_id IN (1, 2, 3, 4, 5, 6)
GROUP BY P.nombrePartido;

# Consulta 5
SELECT D.nombre AS departamento, COUNT(V.id) AS num_votaciones
FROM Departamento AS D
LEFT JOIN Mesa AS M ON D.id = M.id_departamento
LEFT JOIN Votacion AS V ON M.id_mesa = V.mesa_id
GROUP BY D.nombre;

# Consulta 6
SELECT COUNT(id) AS num_votos_nulos
FROM Votacion
WHERE id_candidato = -1;

# Consulta 7
SELECT Edad AS edad, COUNT(*) AS cantidad
FROM Ciudadano
GROUP BY Edad
ORDER BY cantidad DESC, Edad ASC
LIMIT 10;

# Consulta 8
SELECT C.nombres AS candidato, COUNT(V.id) AS num_votos
FROM Candidato AS C
LEFT JOIN Votacion AS V ON C.id = V.id_candidato
WHERE C.cargo_id IN (1, 2)
GROUP BY C.nombres
ORDER BY num_votos DESC
LIMIT 10;

# Consulta 9
SELECT M.id_mesa AS no_mesa, D.nombre AS departamento, COUNT(V.id) AS num_votaciones
FROM Mesa AS M
LEFT JOIN Departamento AS D ON M.id_departamento = D.id
LEFT JOIN Votacion AS V ON M.id_mesa = V.mesa_id
GROUP BY M.id_mesa, D.nombre
ORDER BY num_votaciones DESC
LIMIT 5;

# Consulta 10
SELECT SUBSTR(fecha_hora, 12, 5) AS hora, COUNT(id) AS num_votaciones
FROM Votacion
GROUP BY hora
ORDER BY num_votaciones DESC
LIMIT 5;

# Consulta 11
SELECT Genero AS genero, COUNT(V.id) AS num_votos
FROM Ciudadano AS C
LEFT JOIN Votacion AS V ON C.dpi = V.dpi_ciudadano
GROUP BY Genero;

# Eliminar contenido de tablas temporales
DELETE FROM candidato_temporal;
DELETE FROM cargo_temporal;
DELETE FROM ciudadano_temporal;
DELETE FROM departamento_temporal;
DELETE FROM mesa_temporal;
DELETE FROM partido_temporal;
DELETE FROM votacion_temporal;

# Eliminar contenido de modelos
DELETE FROM candidato;
DELETE FROM cargo;
DELETE FROM ciudadano;
DELETE FROM departamento;
DELETE FROM mesa;
DELETE FROM partido;
DELETE FROM votacion;

    
DROP TEMPORARY TABLE IF EXISTS TempTable;
