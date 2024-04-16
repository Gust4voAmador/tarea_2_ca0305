# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:27:37 2024

@author: AMADOR
"""
from MatrizCuadrada import MatrizNxm,MatrizCuadrada

ma = [[1,1], [1,1]]

mb = [[2,2], [2,2]]

mc = [[2,2,2], [1,1,1],[1,1,1]]

factor = [2,2]

a = MatrizCuadrada("A", ma)
b = MatrizCuadrada("B", mb)
c = MatrizCuadrada("C", mc)

print(b.get_matriz())

print(MatrizCuadrada.funcion_suma(a, b))

print(a.get_matriz())

print(MatrizCuadrada.funcion_multiplicacion(a, factor))

print(MatrizCuadrada.inversa(a))

print(MatrizCuadrada.transpuesta(c))

#a.set_nombre("pepa")
#print(a.get_columnas())

