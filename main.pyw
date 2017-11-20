# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from convocados import *


from pymongo import MongoClient
from Futbolista import *

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
    Futbolista('Iker','Casillas',33,'Portero',1,False),
    Futbolista('Carles','Puyol',36,'Central',2,False),
    Futbolista('Sergio','Ramos',28,'Lateral',1,False),
    Futbolista('Andres','Iniesta',30,'Centrocampista',1,False),
    Futbolista('Fernando','Torres',30,'Delantero',2,False),
    Futbolista('Leo','Baptistao',22,'Delantero',2,False)
    ]


Equipos =[
    equipo(1,'River'),
    equipo(2,'Barcelona')

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
convocados= db.Convocados
equipos.drop()
convocados.drop()

# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista



for futbolista in futbolistas:
    collection.insert(futbolista.toDBCollection())

for equ in Equipos:
    equipos.insert(equ.toDBCollection())


# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()
for fut in cursor:
    print "%s - %s - %i - %s - %r" \
         %(fut['nombre'], fut['apellidos'], fut['edad'], fut['tipo'], fut['equipo'])


global consulta
consulta=[{'$lookup':{
    'from':'Futbolistas',
    'localField': '_id',
    'foreignField' : 'equipo',
    'as': 'miembro'}},
        {'$match':
         {'nombre':'river'}}]

doc=equipos.aggregate(consulta)    
print " jugadores de river"

for f in doc:
    for fut in f["miembro"]:
         print "%s - %s - %i - %s " \
         %(fut['nombre'], fut['apellidos'], fut['edad'], fut['tipo'])

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
        QtCore.QObject.connect(self.ui.agregar_button, QtCore.SIGNAL('clicked()'), self.agregar)
        QtCore.QObject.connect(self.ui.mostrar_button, QtCore.SIGNAL('clicked()'), self.mostrar)
        QtCore.QObject.connect(self.ui.eliminar_button, QtCore.SIGNAL('clicked()'), self.borrar)
        
    def actualizar_convocados(self):
        global convocados
        self.ui.list_convocados.clear()

    #READ leemos todos los documentos de la coleccion convocados
        cursor = convocados.find()
        for fut in cursor:
            self.ui.list_convocados.addItem(fut['nombre'])
            
    def mostrar(self):
        self.ui.list_equipos.clear()
        #text = self.ui.list_equipos.currentItem().text()  // agarra el text del item elejido de la lista
        global collection,equipos,consulta

        #cuando se elija un equipo del combo box, se hara la consulta con el nombre de ese equipo
        equipo_select=self.ui.Equipos_Cbox.currentText()

        # READ : hacemos una consulta usamos el comando lookup para hacer un join entre los dos documentos ( equipo,jugador)
        consulta=[{'$lookup':{
            'from':'Futbolistas',
            'localField': '_id',
            'foreignField' : 'equipo',
            'as': 'miembro'}},
                {'$match':
                 {'nombre':str(equipo_select)}}] 
        
        #Recorremos todo el json d
        doc=equipos.aggregate(consulta)
        for f in doc:
            for fut in f["miembro"]:
                if(fut["convocado"] == False): # condicional que valida si el jugador fue convocado o 
                    a= fut['nombre'] +" "+ fut['apellidos']+" - " + fut['tipo']+ " - edad " +str(fut['edad']) 
                    self.ui.list_equipos.addItem(a)
                      
    def agregar(self):
        global collection,equipos,convocados
        text = str(self.ui.list_equipos.currentItem().text())
        posi= text.find(" ")
        posi2= text.find(" - ")
        jugador=text[0:posi]
        
        #UPDATE:  actualizamos el campo "convocado" a true 
        collection.update({"nombre":jugador},{'$set':{"convocado" : True}})

        jugador=text[0:posi2]
        #INSERT :
        convocados.insert(convocado(jugador).toDBCollection())
        self.ui.list_equipos.takeItem(self.ui.list_equipos.currentRow())
        self.actualizar_convocados()

    def borrar(self):
        
        global convocados
        text = str(self.ui.list_convocados.currentItem().text())
        # el documento del convocado seleccionado se borrara de la coleccion convocados, cuando hagamos click en el boton borrar
        convocados.remove({"nombre":text})
        self.actualizar_convocados()
        
            
        
            
            

    

        

if __name__ == "__main__":


    app= QtGui.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec_())





