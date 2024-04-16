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
        
        #Crear una matriz "A+B" que es la suma pero va a ser la matriz c
        cnxn = anxn
        cnxn.set_nombre("A+B")
        
        # for anidado para que acceda a cada entradas de la matriz y sume
        for i in range(0,anxn.get_filas()):
            for j in range(0,anxn.get_columnas()):
                #sumar entradas
                valor = anxn.get_matriz()[i][j] + bnxn.get_matriz()[i][j] 
                
                #cambiar valor de la entrada por la suma en la matriz "A+B"
                cnxn.set_entrada_matriz(i, j, valor) 
        
        return cnxn
            
    
   
    
    
    
    
    
    
    
    