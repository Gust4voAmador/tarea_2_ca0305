# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:42:18 2024

@author: AMADOR
"""

import numpy as np
import copy

class MatrizNxm():
    
    #el constructor exige un nombre para la matriz como "A" y la matriz es 
    #una lista de listas. Esta clase tiene como requisito que el numero de fi-
    #las y columnas sean distintos.
    def __init__(self, nombre, matriz_nxm):
        
        #atributos
        self.__nombre = nombre
        self.matriz = matriz_nxm
        self.filas = len(matriz_nxm)
        self.columnas = len(matriz_nxm[0])

    
    #Get
    def get_nombre(self): 
        return self.__nombre
        
    def get_filas(self): 
        return self.filas
    
    def get_columnas(self): 
        return self.columnas
    
    def get_matriz(self):
        return self.matriz
    
    #set
    def set_nombre(self, new_name):
        self.__nombre = new_name
        return self.__nombre
    
    def set_entrada_matriz(self, fila, columna, valor):
        # Verificar que fila y columna estén dentro de los límites de la matriz
        if fila < 0 or fila >= len(self.matriz):
            raise IndexError("Índice de fila fuera de rango")
        if columna < 0 or columna >= len(self.matriz[0]):
            raise IndexError("Índice de columna fuera de rango")
    
        # Establecer el valor en la posición especificada
        self.matriz[fila][columna] = valor
    
    
    
    
    #Método str
    def __str__(self):
        # Construir una cadena con el nombre de la matriz 
        matriz_str = f"Matriz '{self.__nombre}':\n"
        #for que se meta en la filas
        for fila in self.matriz:
            #for que recorra las filas
            for i in fila:
                matriz_str += f"{i} "  # Convierte cada int en str
            matriz_str += "\n"
        return matriz_str
    
    
    
    
class MatrizCuadrada(MatrizNxm):
    
    def __init__(self, nombre, matriz_nxm):
        
        MatrizNxm.__init__(self,nombre, matriz_nxm)
        
        # Verificar que no es cuadrada dentro del constructor
        # https://docs.python.org/3/tutorial/errors.html
        #Los atributos filas y cols son privados por lo que se usa get
        if self.get_filas() != self.get_columnas():
            raise ValueError("La matriz debe tener igual número de filas y columnas")
            

    # Función static 
    def funcion_suma(anxn,bnxn):
        
        # https://keepcoding.io/blog/funcion-isinstance-en-python/
        #Verificar que los parametros sean objetos matrizcuadrada
        if not isinstance(anxn, MatrizCuadrada) or not isinstance(bnxn, MatrizCuadrada):
            raise TypeError("El argumento debe ser un objeto de la clase MiClase")
        
        #crear una matriz compia de anxn para tener molde para la matriz suma
        c = []
        
        # Inicializar la nueva matriz con ceros
        for i in range(0,anxn.get_filas()):
            fila = []
            for j in range(0,anxn.get_columnas()):
                fila.append(0)
            c.append(fila)
        
        #Crear un objeto "A+B cuadrada que es la suma pero con la matriz c
        cnxn = MatrizCuadrada(f"{anxn.get_nombre()}+{bnxn.get_nombre()}", c)
    
        # for anidado para que acceda a cada entradas de la matriz y sume
        for i in range(0,anxn.get_filas()):
            for j in range(0,anxn.get_columnas()):
                #sumar entradas
                valor = anxn.get_matriz()[i][j] + bnxn.get_matriz()[i][j] 
                
                #cambiar valor de la entrada por la suma en la matriz "A+B"
                cnxn.set_entrada_matriz(i, j, valor) 
        
        return cnxn
            
    def funcion_multiplicacion(dnxn, factor):
        
        #Verificar que dnxn sea un objeto matirz cuadrada
        if not isinstance(dnxn, MatrizCuadrada):
            raise TypeError("El argumento debe ser un objeto de la clase MatrizCuadrada")
   
        #Caso 1: factor es un escalar (int):
        if isinstance(factor, int):
            #Crear una matriz "factor * A" que es la suma pero va a ser la matriz c
            cnxn = dnxn
            nombre = dnxn.get_nombre()
            cnxn.set_nombre(f"{factor}*" + nombre)
            
            # for anidado para que acceda a cada entradas y multiplique
            for i in range(0,dnxn.get_filas()):
                for j in range(0,dnxn.get_columnas()):
                    #sumar entradas
                    valor = dnxn.get_matriz()[i][j] * factor 
                    
                    #cambiar valor de la entrada por la suma en la matriz "A+B"
                    cnxn.set_entrada_matriz(i, j, valor) 
    
            return cnxn
        
        #Caso 2: factor es un vector (o lista, ya que en py no hay vectores)
        elif isinstance(factor, list):
            #verificar que el vector fila sea adecuado
            if dnxn.get_filas() == len(factor):
                #Crear lista para crear el vector que se retorna
                vector_return = []
                
                # Crear 2 for anidados para acceder a las entradas de la matriz
                for j in range(0, dnxn.get_columnas()): #recorre columnas
                    #iniciar valor que suma los productos
                    valor = 0
                    for i in range(0, dnxn.get_filas()):
                        valor += dnxn.get_matriz()[i][j] * factor[j]
    
                    #agregar elemento a lista return
                    vector_return.append(valor)
    
                #Crear objeto tipo matriz nxm
                cnxm = MatrizNxm(f'{factor}*{dnxn.get_nombre()}', [vector_return],)
                
                return cnxm
            # retornar error si el vector no sirve
            else:
                raise TypeError("El vector debe tener igual catidad de columnas como filas de la matriz")
        
        #retornar error si el factor ingresado no es válido    
        else:
            raise TypeError("El factor debe ser un escalar o un vector de fila cuerente")
    
            
    
    
    #Tiene como parámetro un objeto matriz cuadrada
    def inversa(anxn):
        #extraer la matriz del objeto
        matriz = anxn.get_matriz()
        
        #Calcula la inversa de la matriz con librería de numpy
        try:
            inv = np.linalg.inv(matriz)
            
            #Crear nuevo objeto matriz cuadrada que sea la inversa
            cnxn = MatrizCuadrada(f"{anxn.get_nombre()}^-1", inv)
            
            return cnxn
        
        except np.linalg.LinAlgError:
            print(f'La matriz {anxn.get_nombre()} no es invertible')
        
        
        
    def transpuesta(anxn):
        #extraer la matriz del objeto
        matriz = anxn.get_matriz()
        
        #crear copia de la matriz para tener el molde para transpuesta
        trans = copy.deepcopy(matriz)
        
        
        #Realizar la operacion con for anidados
        for i in range(0,anxn.get_filas()):
            for j in range(0,anxn.get_columnas()):
                trans[i][j] = matriz[j][i]
        
        
        #Crear un objeto "A^T cuadrada que es la transpuesta de A
        transpuesta = MatrizCuadrada(f"{anxn.get_nombre()}^T", trans)
        
        return transpuesta
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    