# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:27:37 2024

@author: AMADOR
"""

import numpy as np
from MatrizCuadrada import MatrizNxm,MatrizCuadrada
ma = [[1,1], [1,1]]

mb = [[2,2], [2,2]]

mc = [[2,2,2], [1,1,1],[1,1,1]]

md = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]    




a = MatrizCuadrada("A", ma)
b = MatrizCuadrada("B", mb)
c = MatrizCuadrada("C", mc)
d = MatrizCuadrada("D", md)

factor = [2,2]
print(np.array(factor).shape)

#print(len(factor[0]))
print(isinstance(factor, list))


print(b.get_matriz)

print(MatrizCuadrada.funcion_suma(a, b))

print(a.get_matriz)

print(MatrizCuadrada.funcion_multiplicacion(a, mb))

#print(MatrizCuadrada.inversa(a))

#print(MatrizCuadrada.transpuesta(c))

#print(MatrizCuadrada.valores_propios(d))

#print(MatrizCuadrada.vectores_propios(d))

#print(MatrizCuadrada.valores_singulares(d))

#a.set_nombre("pepa")
#print(a.get_columnas())

#Probar la A^3




#print("Probar A^3")
x = [[0,2,-1],[0,0,1],[0,0,0]]

A = MatrizCuadrada("A", x)

A_2 = MatrizCuadrada.funcion_multiplicacion(A, A)

#print('A^2')
#print(A_2)

A_3 = MatrizCuadrada.funcion_multiplicacion(A_2, A)

#print(A_3)

#print("Probar Polinomio")

I = MatrizCuadrada("I", [[1,0,0], [0,1,0],[0,0,1]])


A_I = MatrizCuadrada.funcion_suma(I, A)
#print(A_I)

#Hacer la matriz A_2 del tipo cuadrada
A_2_cuadra = MatrizCuadrada("A_I", A_2.get_matriz)

I_A_A2 = MatrizCuadrada.funcion_suma(A_I, A_2_cuadra)

#print(I_A_A2)

#print(MatrizCuadrada.inversa(MatrizCuadrada("ImenosA", [[1,-2,1],[0,1,-1],[0,0,1]])))


