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
        """
        Constructor de la clase MatrizNxm.
        
        Parámetros:
            nombre (str): Nombre de la matriz.
            matriz_nxm (list of lists): Matriz como lista de listas.
        
        Requisitos:
            El número de filas y columnas deben ser distintos.
        """
        
        #atributos
        self.__nombre = nombre
        self.matriz = matriz_nxm
        self.filas = len(matriz_nxm)
        self.columnas = len(matriz_nxm[0])

    
    @property
    def get_nombre(self): 
        """
        Método getter para obtener el nombre de la matriz.
        """
        return self.__nombre
    
    @property    
    def get_filas(self):
        """
        Método getter para obtener el número de filas de la matriz.
        """
        return self.filas
    
    @property
    def get_columnas(self): 
        """
        Método getter para obtener el número de columnas de la matriz.
        """
        return self.columnas
    
    @property
    def get_matriz(self):
        """
        Método getter para obtener la matriz.
        """
        return self.matriz
    
    @get_nombre.setter
    def set_nombre(self, new_name):
        """
        Método setter para cambiar el nombre de la matriz.

        Parámetros:
            new_name (str): Nuevo nombre para la matriz.
        
        Retorna:
            str: El nuevo nombre de la matriz.
        """
        self.__nombre = new_name
        return self.__nombre
    
    @get_filas.setter
    def set_filas(self, new_filas):
        """
        Setter para actualizar el número de filas.

        :param new_filas: El nuevo número de filas.
        :type new_filas: int
        """
        self.__filas = new_filas
    
    @get_columnas.setter
    def set_columnas(self, new_columnas):
        """
        Setter para actualizar el número de columnas.

        :param new_columnas: El nuevo número de columnas.
        :type new_columnas: int
        """
        self.__columnas = new_columnas
        
    @get_matriz.setter
    def set_matriz(self, new_matriz):
        """
        Método setter para cambiar la matriz.

        Parámetros:
            new_matriz (list of lists): Nueva matriz como lista de listas.
        
        Retorna:
            list of lists: La nueva matriz.
        
        Raises:
            ValueError: Si el parámetro no es una matriz (lista de listas).
        """
        if isinstance(new_matriz[0], list):
            self.matriz = new_matriz
            return self.matriz
        else:
            raise ValueError("El parámetro debe ser una matriz (lista de listas)")
            
            
    #Método para modificar una entrada del atributo matriz
    def set_entrada_matriz(self, fila, columna, valor):
        """
        Método para modificar una entrada específica de la matriz.

        Parámetros:
            fila (int): Índice de la fila.
            columna (int): Índice de la columna.
            valor: Nuevo valor para la entrada especificada.
        
        Raises:
            IndexError: Si el índice de fila o columna está fuera de rango.
        """
        # Verificar que fila y columna estén dentro de los límites de la matriz
        if fila < 0 or fila >= len(self.matriz):
            raise IndexError("Índice de fila fuera de rango")
        if columna < 0 or columna >= len(self.matriz[0]):
            raise IndexError("Índice de columna fuera de rango")
    
        # Establecer el valor en la posición especificada
        self.matriz[fila][columna] = valor
    
    
    
    
    #Método str
    def __str__(self):
        """
        Método para representar la matriz como una cadena.

        Retorna:
            str: Representación de la matriz como una cadena.
        """
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
        """
        Constructor de la clase MatrizCuadrada.

        Parámetros:
            nombre (str): Nombre de la matriz.
            matriz_nxm (list of lists): Matriz como lista de listas.
        
        Raises:
            ValueError: Si la matriz no es cuadrada.
        """
        
        MatrizNxm.__init__(self,nombre, matriz_nxm)
        
        # Verificar que no es cuadrada dentro del constructor
        # https://docs.python.org/3/tutorial/errors.html
        #Los atributos filas y cols son privados por lo que se usa get
        if self.get_filas != self.get_columnas:
            raise ValueError("La matriz debe tener igual número de filas y columnas")
    
    @property
    def get_matriz(self):
        """
        Método getter para obtener la matriz.
        """
        return self.matriz
    
    @get_matriz.setter        
    def set_matriz_cuadrada(self, new_matriz):
        """
        Método setter para cambiar la matriz cuadrada.

        Parámetros:
            new_matriz (list of lists): Nueva matriz como lista de listas.
        
        Retorna:
            list of lists: La nueva matriz.
        
        Raises:
            ValueError: Si la nueva matriz no es cuadrada.
        """
        #Verificar que la nueva matriz satisfaga condiciones para se aceptable
        if not isinstance(new_matriz[0], list): 
            raise ValueError("El parámetro debe ser una matriz (lista de listas)")
        elif len(new_matriz[0]) != len(new_matriz):
            raise ValueError("La nueva matriz debe tener igual número de filas y columnas")   
        else:        
            self.matriz = new_matriz
            return self.matriz
            

    # Función estática para sumar dos matrices cuadradas
    @staticmethod 
    def funcion_suma(anxn,bnxn):
        """
        Función estática para sumar dos matrices cuadradas.

        Parámetros:
            anxn (MatrizCuadrada): Primera matriz cuadrada.
            bnxn (MatrizCuadrada): Segunda matriz cuadrada.
        
        Retorna:
            MatrizCuadrada: La suma de las dos matrices cuadradas.
        
        Raises:
            TypeError: Si alguno de los argumentos no es un objeto de la clase MatrizCuadrada.
        """
        
        # https://keepcoding.io/blog/funcion-isinstance-en-python/
        #Verificar que los parametros sean objetos matrizcuadrada
        if not isinstance(anxn, MatrizCuadrada) or not isinstance(bnxn, MatrizCuadrada):
            raise TypeError("El argumento debe ser un objeto de la clase MatrizCuadrada")
        
        #crear una matriz compia de anxn para tener molde para la matriz suma
        c = []
        
        # Inicializar la nueva matriz con ceros
        for i in range(0,anxn.get_filas):
            fila = []
            for j in range(0,anxn.get_columnas):
                fila.append(0)
            c.append(fila)
        
        #Crear un objeto "A+B cuadrada que es la suma pero con la matriz c
        cnxn = MatrizCuadrada(f"{anxn.get_nombre}+{bnxn.get_nombre}", c)
    
        # for anidado para que acceda a cada entradas de la matriz y sume
        for i in range(0,anxn.get_filas):
            for j in range(0,anxn.get_columnas):
                #sumar entradas
                valor = anxn.get_matriz[i][j] + bnxn.get_matriz[i][j] 
                
                #cambiar valor de la entrada por la suma en la matriz "A+B"
                cnxn.set_entrada_matriz(i, j, valor) 
        
        return cnxn
    
    # Función estática para convertir un array de NumPy en matriz
    @staticmethod
    def array_a_vector(array, num_columnas):
        """
        Función estática para convertir un array de NumPy en matriz.

        Parámetros:
            array (numpy.ndarray): Array de NumPy.
            num_columnas (int): Número de columnas de la matriz.
        
        Retorna:
            list of lists: La matriz resultante.
        
        Raises:
            ValueError: Si el tamaño del array no es compatible con el número de columnas proporcionado.
        """
        lista_de_listas = []
        fila_actual = []
    
        for elemento in array:
            fila_actual.append(elemento)
            if len(fila_actual) == num_columnas:
                lista_de_listas.append(fila_actual)
                fila_actual = []
    
        if fila_actual:
            raise ValueError("El tamaño del array no es compatible con el número de columnas proporcionado.")
    
        return lista_de_listas
    
    def array_a_matriz(array, num_columnas):
        """
        Convierte un array de NumPy en una matriz representada como una lista de listas.
    
        Esta función toma un array de una dimensión y lo convierte en una matriz de varias filas,
        donde el número de columnas está especificado por el parámetro `num_columnas`.
    
        Parámetros:
            array (numpy.ndarray): El array de una dimensión que se convertirá en matriz.
            num_columnas (int): El número de columnas deseado para la matriz.
    
        Retorna:
            list of lists: La matriz resultante, representada como una lista de listas.
    
        Raises:
            None
        """
        return [fila.tolist() for fila in array]
    

    # Función estática para multiplicar un objeto MatrizCuadrada por algo
    @staticmethod        
    def funcion_multiplicacion(obj_matriz_nxn, factor):
        """
        Función estática para multiplicar una matriz cuadrada (objeto MatrizCuadrada) por un factor.

        Parámetros:
            obj_matriz_nxn (objeto de tipo MatrizCuadrada): Matriz cuadrada a multiplicar.
            factor (int, float, list,list of list ,tipo MatrizCuadrada): Factor de multiplicación.

        Retorna:
            Objeto de tipo MatrizNxm: La matriz resultante de la multiplicación.
        
        Raises:
            TypeError: Si el primer parámetro no es un objeto de la clase MatrizCuadrada o MatrizNxm.
            TypeError: Si la multiplicación no es posible entre la matriz y el factor proporcionado.
            TypeError: Si el factor proporcionado no es válido.
        """
        # Verificar que obj_matriz_nxn sea un objeto matriz cuadrada
        if not isinstance(obj_matriz_nxn, (MatrizCuadrada,MatrizNxm)):
            raise TypeError("El primer parámetro debe ser un objeto de la clase MatrizCuadrada o MatrizNxm")
        
        # Caso 1: si el factor es una matriz o un vector (lista de listas o lista simple)
        if isinstance(factor, list):
            # Verificar si el factor es una matriz (lista de listas) o un vector (lista simple)
            if isinstance(factor[0], list):
                # Si el factor es una matriz
                # Verificar si las matrices son compatibles
                if obj_matriz_nxn.get_columnas() != len(factor[0]):
                    raise TypeError("No se pueden multiplicar. El número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz.")
                
                # Convertir la matriz y el vector a arrays de NumPy
                matriz = np.array(obj_matriz_nxn.get_matriz())
                matriz_2 = np.array(factor)
                
                # Usar NumPy para hacer la multiplicacion
                matriz_producto = np.dot(matriz, matriz_2)
                
                # Crear objeto MatrizNxm con la matriz producto para retornarlo
                # tolist() es para convertir el array a matriz otra vez
                obj_matriz_producto = MatrizNxm("Matriz producto", MatrizCuadrada.array_a_matriz(matriz_producto, obj_matriz_nxn.get_columnas()))
                
                return obj_matriz_producto
            
            else: 
                # Si el factor es un vector (elementos son float)
                # Verificar si la matriz y el vector son compatibles 
                if obj_matriz_nxn.get_columnas() != len(factor):
                    raise TypeError("No se pueden multiplicar la matriz y el vector. El número de columnas de la matriz no coincide con el número de elementos del vector.")
                 
                # Convertir la matriz y el vector a arrays de NumPy
                matriz = np.array(obj_matriz_nxn.get_matriz())
                vector = np.array(factor)
                 
                # Usar NumPy para hacer la multiplicacion
                matriz_producto = np.dot(matriz, vector)
                 
                # Crear objeto MatrizNxm con la matriz producto para retornarlo
                # tolist() es para convertir el array a matriz otra vez
                
                obj_matriz_producto = MatrizNxm("Matriz producto", MatrizCuadrada.array_a_vector(matriz_producto, obj_matriz_nxn.get_columnas()))
                
                 
                return obj_matriz_producto 


        #Caso 2: si el factor es una matriz objeto de la clase MatrizNxm o MatrizCaudrada
        if isinstance(factor, MatrizNxm) or isinstance(factor, MatrizCuadrada):
            
            # Verificar si las matrices son son compatibles
            if obj_matriz_nxn.get_columnas != factor.get_filas:
                raise TypeError("No se pueden multiplicar. El número de columnas de la primera matriz no coincide con el numero de filas de la segunda matriz")
            
            # Convertir las matrices a arrays de NumPy
            matriz_1 = np.array(obj_matriz_nxn.get_matriz)
            matriz_2 = np.array(factor.get_matriz)
            
            #Usar NumPy para hacer la multiplicacion
            matriz_producto = np.dot(matriz_1, matriz_2)
        
            #Crear objeto MatrizNxm con la matriz producto para retornarlo
            #tolist() es para convertir el array a matriz otra vez
            obj_matriz_producto = MatrizNxm("Producto", matriz_producto.tolist())
            
            return obj_matriz_producto
        
        
        #Caso 3: si el factor es un escalar   
        elif isinstance(factor, float) or isinstance(factor, int) :
            
            # Convertir la matriz a arrays de NumPy
            matriz = np.array(obj_matriz_nxn.get_matriz)
        
            #Multiplicar escalar con la matriz
            matriz_producto = matriz * factor
        
            #Crear objeto MatrizNxm con la matriz producto para retornarlo
            #tolist() es para convertir el array a matriz otra vez
            obj_matriz_producto = MatrizNxm("Producto", matriz_producto.tolist())
            
            return obj_matriz_producto

        
        #retornar error si el factor ingresado no es válido    
        else:
            raise TypeError("El factor es inválito, solo admite objetos del tipo MatrizNxm, MatrizCuadrada, matriz (lista de listas), vector (lista) y escalares (int o float)") 
            

    # Función estática para calcular la inversa de una matriz cuadrada
    @staticmethod
    def inversa(anxn):
        """
        Función estática para calcular la inversa de una matriz cuadrada.

        Parámetros:
            anxn (MatrizCuadrada): Matriz cuadrada.

        Retorna:
            MatrizCuadrada: La inversa de la matriz cuadrada.

        Raises:
            TypeError: Si el parámetro no es un objeto de la clase MatrizCuadrada.
        """
        #Verificar que anxn sea un objeto matirz cuadrada
        if not isinstance(anxn, MatrizCuadrada):
            raise TypeError("El parámetro debe ser un objeto de la clase MatrizCuadrada")
        
        #extraer la matriz del objeto
        matriz = anxn.get_matriz
        
        #Calcula la inversa de la matriz con librería de numpy
        try:
            inv = np.linalg.inv(matriz)
            
            #Crear nuevo objeto matriz cuadrada que sea la inversa
            cnxn = MatrizCuadrada(f"{anxn.get_nombre}^-1", inv.tolist())
            
            return cnxn
        
        except np.linalg.LinAlgError:
            print(f'La matriz {anxn.get_nombre} no es invertible')
        
        
        
    # Función estática para calcular la transpuesta de una matriz cuadrada
    @staticmethod
    def transpuesta(anxn):
        """
        Función estática para calcular la transpuesta de una matriz cuadrada.

        Parámetros:
            anxn (MatrizCuadrada): Matriz cuadrada.

        Retorna:
            MatrizCuadrada: La transpuesta de la matriz cuadrada.

        Raises:
            TypeError: Si el parámetro no es un objeto de la clase MatrizCuadrada.
        """
        #Verificar que anxn sea un objeto matirz cuadrada
        if not isinstance(anxn, MatrizCuadrada):
            raise TypeError("El parámetro debe ser un objeto de la clase MatrizCuadrada")
        
        #extraer la matriz del objeto
        matriz = anxn.get_matriz
        
        #crear copia de la matriz para tener el molde para transpuesta
        trans = copy.deepcopy(matriz)
        
        
        #Realizar la operacion con for anidados
        for i in range(0,anxn.get_filas):
            for j in range(0,anxn.get_columnas):
                trans[i][j] = matriz[j][i]
        
        
        #Crear un objeto "A^T cuadrada que es la transpuesta de A
        transpuesta = MatrizCuadrada(f"{anxn.get_nombre()}^T", trans.tolist())
        
        return transpuesta
        
        
    # Función estática para calcular los valores propios de una matriz cuadrada
    @staticmethod
    def valores_propios(anxn):
        """
        Función estática para calcular los valores propios de una matriz cuadrada.

        Parámetros:
            anxn (MatrizCuadrada): Matriz cuadrada.

        Retorna:
            numpy.ndarray: Los valores propios de la matriz cuadrada.

        Raises:
            TypeError: Si el parámetro no es un objeto de la clase MatrizCuadrada.
        """
        
        #Verificar que anxn sea un objeto matirz cuadrada
        if not isinstance(anxn, MatrizCuadrada):
            raise TypeError("El parámetro debe ser un objeto de la clase MatrizCuadrada")
        
        #obtener matriz 
        matri = anxn.get_matriz
        
        # Definir la matriz segun np para usar la librería
        matriz = np.array(matri)
        
        # Calcular los valores propios
        vp = np.linalg.eigvals(matriz)
               
        return vp
        
        
    # Función estática para calcular los vectores propios de una matriz cuadrada
    @staticmethod
    def vectores_propios(anxn):
        """
        Función estática para calcular los vectores propios de una matriz cuadrada.

        Parámetros:
            anxn (MatrizCuadrada): Matriz cuadrada.

        Retorna:
            numpy.ndarray: Los vectores propios de la matriz cuadrada.

        Raises:
            TypeError: Si el parámetro no es un objeto de la clase MatrizCuadrada.
        """
        #Verificar que anxn sea un objeto matirz cuadrada
        if not isinstance(anxn, MatrizCuadrada):
            raise TypeError("El parámetro debe ser un objeto de la clase MatrizCuadrada")
        
        #obtener matriz 
        matriz = anxn.get_matriz
        
        # Calcular vectores propios
        valores_propios, vectores_propios = np.linalg.eig(matriz)
        
        # Devolver los vectores propios
        return vectores_propios    
    
        
    # Función estática para calcular los valores singulares de una matriz cuadrada
    @staticmethod
    def valores_singulares(anxn):
        """
        Función estática para calcular los valores singulares de una matriz cuadrada.

        Parámetros:
            anxn (MatrizCuadrada): Matriz cuadrada.

        Retorna:
            dict: Un diccionario con los valores singulares 'U', 'S' y 'V^T' de la matriz cuadrada.

        Raises:
            TypeError: Si el parámetro no es un objeto de la clase MatrizCuadrada.
        """
        #Verificar que anxn sea un objeto matirz cuadrada
        if not isinstance(anxn, MatrizCuadrada):
            raise TypeError("El parámetro debe ser un objeto de la clase MatrizCuadrada")    
        
        #obtener matriz 
        matri = anxn.get_matriz
        
        # Definir una matriz para numpy
        matriz = np.array(matri)
            
        # Calcular la SVD
        U, S, VT = np.linalg.svd(matriz)
        
        #Crear diccionario con los valores singulares obtenidos
        dicci = {
        'U': U,
        "S": S,
        "V^T": VT
        }
        
        return dicci
        
        
        
        
        
        
        
    
    
    
    