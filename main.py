# -*- coding: utf-8 -*-
from pymongo import MongoClient
from Futbolista import Futbolista
from Futbolista import equipo

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
    Futbolista('Iker','Casillas',33,'Portero',1),
    Futbolista('Carles','Puyol',36,'Central',2),
    Futbolista('Sergio','Ramos',28,'Lateral',1),
    Futbolista('Andrés','Iniesta',30,'Centrocampista',1),
    Futbolista('Fernando','Torres',30,'Delantero',2),
    Futbolista('Leo','Baptistao',22,'Delantero',2)
    ]

river= {'juan':'perez','jose':'aquino'}
barcel= {'pedro':'rodrigz','carlos':'kaka'}
Equipos =[
    equipo(1,'river'),
    equipo(2,'barcelona')

    ]
# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.Futbol


# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db.Futbolistas
collection.drop()
equipos = db.Equipos
equipos.drop()


# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista
for futbolista in futbolistas:
    collection.insert(futbolista.toDBCollection())

for equ in Equipos:
    equipos.insert(equ.toDBCollection())


# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()
print cursor
for fut in cursor:
    print "%s - %s - %i - %s - %r" \
         %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional'])




mienbr=[{'$lookup':{
    'from':'Futbolistas',
    'localField': '_id',
    'foreignField' : 'internacional',
    'as': 'miembro'}},
        {'$match':
         {'nombre':'river'}}]

doc=equipos.aggregate(mienbr)
print " jugadores de river"

for f in doc:
    for fut in f["miembro"]:
         print "%s - %s - %i - %s " \
         %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'])


         
    

    


collection.drop()
equipos.drop()
# PASO FINAL: Cerrar la conexion
mongoClient.close()

