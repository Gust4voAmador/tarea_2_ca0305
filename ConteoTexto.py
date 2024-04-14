# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:31:19 2024

@author: AMADOR
"""
def conteo_palabras(frase):
    
    #separar frase en palabras y ponerlos en una lista
    lista_palabras = frase.split()
    
    #utilizar set para obtener una lista de las palabras no repetidas
    set_palabras = list(set(lista_palabras))
    
    #Crar diccionario vacío para guardar el número de palabras en la frase
    dicc_cont_palabras = {}
    
    #iniciar un for para realizar el conteo
    for palabra in set_palabras:
        contador = 0
        for palabra_rep in lista_palabras:
            if palabra == palabra_rep:
                contador = contador + 1
    
        dicc_cont_palabras[palabra] = contador
    
    return dicc_cont_palabras
   
#conteo = conteo_palabras("Hola como estas como ja ja jaj ja")
#print(conteo)



    







