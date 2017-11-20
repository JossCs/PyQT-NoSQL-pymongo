# -*- coding: utf-8 -*-

class Futbolista:

    def __init__(self,nombre, apellidos, edad, demarcacion, equipo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.equipo=equipo

    def toDBCollection (self):
        jugador = {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.equipo
        }
        return jugador

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.equipo)



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

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.internacional)

