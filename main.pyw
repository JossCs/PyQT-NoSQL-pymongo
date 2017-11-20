# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from convocados import *


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


Equipos =[
    equipo(1,'river'),
    equipo(2,'barcelona')

    ]
# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.Futbol


# PASO 3: Obtenemos una coleccion para trabajar con ella

global collection,equipos
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


global consulta
consulta=[{'$lookup':{
    'from':'Futbolistas',
    'localField': '_id',
    'foreignField' : 'internacional',
    'as': 'miembro'}},
        {'$match':
         {'nombre':'river'}}]

doc=equipos.aggregate(consulta)
print " jugadores de river"

for f in doc:
    for fut in f["miembro"]:
         print "%s - %s - %i - %s " \
         %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'])

         a= fut['nombre'] +" "+ fut['apellidos']
         print a
    

    


#collection.drop()
#equipos.drop()
# PASO FINAL: Cerrar la conexion
mongoClient.close()



class Miformulario(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.list_equipos.addItem("tu mama")
        QtCore.QObject.connect(self.ui.agregar_button, QtCore.SIGNAL('clicked()'), self.agregar)


    def agregar(self):
        text = self.ui.list_equipos.currentItem().text()
        #self.ui.list_equipos.takeItem(self.ui.list_equipos.currentRow())
        self.ui.list_convocados.addItem(text)
        print text
        global collection,equipos,consulta
#se hace la consulta para 
        doc=equipos.aggregate(consulta)
        for f in doc:
             for fut in f["miembro"]:
                 print "%s - %s - %i - %s " \
                 %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'])

                 a= fut['nombre'] +" "+ fut['apellidos']
                 self.ui.list_convocados.addItem(a)
    
            
        


    

        

if __name__ == "__main__":


    app= QtGui.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec_())





