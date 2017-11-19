# -*- coding: utf-8 -*-

class Futbolista:

    def __init__(self, nombre, apellidos, edad, demarcacion, internacional):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.internacional = internacional

    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.internacional)
