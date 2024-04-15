# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:42:18 2024

@author: AMADOR
"""
class MatrizNxm():
    
    #el constructor exige un nombre para la matriz como "A" y la matriz es 
    #una lista de listas. Esta clase tiene como requisito que el numero de fi-
    #las y columnas sean distintos.
    
    def __init__(self, nombre, matriz_nxm):
        self.__nombre = nombre
        self.__matriz = matriz_nxm
        self.__filas = len(matriz_nxm)
        self.__columnas = len(matriz_nxm[0])

        # Verificar que no es cuadrada dentro del constructor
        # https://docs.python.org/3/tutorial/errors.html
        if self.__filas == self.__columnas:
            raise ValueError("La matriz no debe tener igual número de filas y columnas")
    
    #Get
    def get_nombre(self): 
        return self.__nombre
        
    def get_filas(self): 
        return self.__filas
    
    def get_columnas(self): 
        return self.__columnas
    
    #set
    def set_nombre(self, new_name):
        self.__nombre = new_name
        return self.__nombre
    
    #Método str
    def __str__(self):
        # Construir una cadena con el nombre de la matriz 
        matriz_str = f"Matriz '{self.__nombre}':\n"
        #for que se meta en la filas
        for fila in self.__matriz:
            #for que recorra las filas
            for i in fila:
                matriz_str += f"{i} "  # Convierte cada int en str
            matriz_str += "\n"
        return matriz_str
    
    
#class Cuadrada(MatrizNxm):
    