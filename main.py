# -*- coding: utf-8 -*-
from pymongo import MongoClient
from Futbolista import Futbolista

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
    Futbolista('Iker','Casillas',33,['Portero'],True),
    Futbolista('Carles','Puyol',36,['Central', 'Lateral'],True),
    Futbolista('Sergio','Ramos',28,['Lateral','Central'],True),
    Futbolista('Andrés','Iniesta',30,['Centrocampista','Delantero'],True),
    Futbolista('Fernando','Torres',30,['Delantero'],True),
    Futbolista('Leo','Baptistao',22,['Delantero'],False)
    ]


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.Futbol


# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db.Futbolistas

equipos = db.Equipos


# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista
for futbolista in futbolistas:
    collection.insert(futbolista.toDBCollection())


# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()
for fut in cursor:
    print "%s - %s - %i - %s - %r" \
          %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional'])




collection.drop()
equipos.drop()
# PASO FINAL: Cerrar la conexion
mongoClient.close()
