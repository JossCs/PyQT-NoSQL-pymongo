# -*- coding: utf-8 -*-

class Futbolista:

    def __init__(self,nombre, apellidos, edad, tipo, equipo,convocado):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.tipo = tipo
        self.equipo=equipo
        self.convocado=convocado
    #no especifico un _id para jugador
    def toDBCollection (self):
        jugador = {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad": self.edad,
            "tipo":self.tipo,
            "equipo":self.equipo,
            "convocado":self.convocado
        }
        return jugador

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - tipo: %s - equipo: %r" \
               %(self.nombre, self.apellidos, self.edad, self.tipo, self.equipo)



class equipo:

    def __init__(self,_id,nombre):
        self._id=_id
        self.nombre = nombre
    def toDBCollection (self):
        Equipo = {
            "_id":self._id,
            "nombre":self.nombre,
        }
        return Equipo

class convocado:
    def __init__(self,nombre):
        self.nombre = nombre
    def toDBCollection (self):
        Convocado = {
            "nombre":self.nombre,
        }
        return Convocado
    
