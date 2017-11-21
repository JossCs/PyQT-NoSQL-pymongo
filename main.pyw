# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from convocados import *


from pymongo import MongoClient
from Futbolista import *

# Creo una lista de objetos futbolista a insertar en la BD
futbolistas = [
    Futbolista('Iker','Casillas',33,'Portero',1,False),
    Futbolista('Pedro','Gallese',29,'Delantero',4,False),
    Futbolista('Carles','Puyol',36,'Central',2,False),
    Futbolista('Sergio','Ramos',28,'Lateral',1,False),
    Futbolista('Andres','Iniesta',30,'Central',1,False),
    Futbolista('Fernando','Torres',30,'Delantero',2,False),
    Futbolista('Paolo','Guerrero',31,'Delantero',3,False),
    Futbolista('Miguel','Trauco',25,'Defensa',3,False),
    Futbolista('Aldo','Corzo',26,'Delantero',4,False),
    Futbolista('Miguel','Araujo',25,'Defensa',5,False),
    Futbolista('Pedro','Aquino',27,'Central',5,False),
    Futbolista('Leo','Baptistao',22,'Delantero',2,False),
    Futbolista('Renato','Tapia',30,'Central',5,False)
    ]


Equipos =[
    equipo(1,'River'),
    equipo(2,'Barcelona'),
    equipo(3,'Flamengo'),
    equipo(4,'Universitario'),
    equipo(5,'Alianza Lima')

    ]
# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.Futbol


# PASO 3: Obtenemos una coleccion para trabajar con ella


jugadores = db.Futbolistas
equipos = db.Equipos
convocados= db.Convocados
jugadores.drop()
equipos.drop()
convocados.drop()

# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista y equipo (o documentos en Mongo) en la coleccion Futbolista


for futbolista in futbolistas:
    jugadores.insert(futbolista.toDBCollection())

for equ in Equipos:
    equipos.insert(equ.toDBCollection())

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
        QtCore.QObject.connect(self.ui.eliall_button, QtCore.SIGNAL('clicked()'), self.borrartodos)
        QtCore.QObject.connect(self.ui.ingresar_button, QtCore.SIGNAL('clicked()'), self.ingresar_jugador)
        
    def actualizar_convocados(self):
        global convocados
        self.ui.list_convocados.clear()

        #READ leemos todos los documentos de la coleccion convocados
        cursor = convocados.find()
        for fut in cursor:
            self.ui.list_convocados.addItem(fut['nombre'])
            
    def mostrar(self):
        self.ui.list_equipos.clear()
        global jugadores,equipos,consulta

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
        
        #Recorremos todo el json DOC,que contiene el resultado de $lookup
        doc=equipos.aggregate(consulta)
        for f in doc:
            for fut in f["miembro"]:
                # condicional que valida si un jugador es convodado o no,mientras no sea convocado se mostrara
                if(fut["convocado"] == False):  
                    a= fut['nombre'] +" "+ fut['apellidos']+" - " + fut['tipo']+ " - edad " +str(fut['edad']) 
                    self.ui.list_equipos.addItem(a)
                      
    def agregar(self):
        global jugadores,equipos,convocados
        text = str(self.ui.list_equipos.currentItem().text())
        posi= text.find(" ")
        posi2= text.find(" - ")
        jugador=text[0:posi]
        
        #UPDATE:  actualizamos el campo "convocado" a true 
        jugadores.update({"nombre":jugador},{'$set':{"convocado" : True}})

        jugador=text[0:posi2]
        
        #CREATE : insertamos el documento que contiene al jugador convocado en la colleccion convocados
        convocados.insert(convocado(jugador).toDBCollection())
        self.ui.list_equipos.takeItem(self.ui.list_equipos.currentRow())
        self.actualizar_convocados()

    def borrar(self):
        
        global convocados,jugadores
        text = str(self.ui.list_convocados.currentItem().text())
        posi= text.find(" ")
        jugador=text[0:posi]
        #DELETE el documento del convocado seleccionado se borrara de la coleccion convocados, cuando hagamos click en el boton borrar
        convocados.remove({"nombre":text})
        
        #UPDATE actualizamos el campo "convocado"  a False de la coleccion de jugadores
        jugadores.update({"nombre":jugador},{'$set':{"convocado" : False}})
        self.actualizar_convocados()
        
    def borrartodos(self):
        global convocados
        convocados.drop()
        self.actualizar_convocados()      
            
            
    def ingresar_jugador(self):
        global jugadores
        nom = str(self.ui.nombre_text.text())
        ape = str(self.ui.apellido_text.text())
        edad = self.ui.edad_SB.value()
        tipo = str(self.ui.Tipo_CB.currentText())
        equi = self.ui.Equipos_CB.currentIndex()+1

        
        nuevo= Futbolista(nom,ape,edad,tipo,equi,False)

        #CREATE insertamos un nuevo documento (objeto futbolista) a la coleccion Futbolistas
        jugadores.insert(nuevo.toDBCollection())
        
        
        self.ui.nombre_text.clear()
        self.ui.apellido_text.clear()
        edad= self.ui.edad_SB.setValue(20)
        
        

if __name__ == "__main__":


    app= QtGui.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec_())





