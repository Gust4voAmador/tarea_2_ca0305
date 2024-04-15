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


def conteo_letras(frase):
    #Obtener lista con las palabra de la frase sin repetidas
    set_palabras = list(set(frase.split()))
    
    dicc_grande = {}
    
    #for que recorra el set de palabras
    for palabra in set_palabras:
        dicc_palabra = {} 
        
        #crear una lista con las letras sin repetir
        lista_letras = list(palabra)
        set_letras = list(set(lista_letras))
        
        #for que recorra las letras sin repetir
        for letra in set_letras:
            
            contador = 0
            #for que cuente las veces que aparece cada letra
            for caracter in lista_letras:
                
                #condición para que cuente
                if letra == caracter:
                    contador = contador + 1
                    
            #agregar letra y respectivas apariciones en la palabra       
            dicc_palabra[letra] = contador   
            
        #agragar diccionario respectivo a cada palabra con las letras repetidas  
        dicc_grande[palabra] = dicc_palabra


    return dicc_grande


pepe = conteo_letras('Holaoooooo oo mundu')

print(pepe)






