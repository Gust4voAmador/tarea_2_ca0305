# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:17:41 2024

@author: AMADOR
"""
class AnalizadorTexto:
    """
    Clase para analizar texto.
    """
    
    # Constructor método
    def __init__(self, frase):
        """
        Constructor de la clase.

        :param frase: La frase a analizar.
        :type frase: str
        """
        # atributos
        self.frase = frase
    
    @property 
    def get_frase(self):
        """
        Getter para obtener la frase actual.

        :return: La frase actual.
        :rtype: str
        """
        return self.frase
    
    @get_frase.setter
    def set_frase(self, nueva_frase):
        """
        Setter para actualizar la frase.

        :param nueva_frase: La nueva frase.
        :type nueva_frase: str
        """
        self.frase = nueva_frase
    
    def conteo_palabras(self):
        """
       Método de la clase AnalizadorTexto para contar 
       las palabras en la frase.

       :return: Un diccionario con el conteo de cada palabra.
       :rtype: dict
       """       
        
        # Separar frase en palabras y ponerlos en una lista
        lista_palabras = self.get_frase.split()
        # Utilizar set para obtener una lista de las palabras no repetidas
        set_palabras = list(set(lista_palabras))
        # Crar diccionario vacío para guardar el número de palabras en la frase
        dicc_cont_palabras = {}
        # Iniciar un for para realizar el conteo
        for palabra in set_palabras:
            contador = 0
            for palabra_rep in lista_palabras:
                if palabra == palabra_rep:
                    contador += 1
            dicc_cont_palabras[palabra] = contador
        return dicc_cont_palabras

    def conteo_letras(self):
        """
        Método de la clase AnalizadorTexto 
        para contar las letras en cada palabra de la frase.

        :return: Un diccionario anidado con el conteo de cada letra en cada palabra.
        :rtype: dict
        """
        # Obtener lista con las palabra de la frase sin repetidas
        set_palabras = list(set(self.get_frase.split()))
        dicc_grande = {}
        # For que recorra el set de palabras
        for palabra in set_palabras:
            dicc_palabra = {}
            # Crear una lista con las letras sin repetir
            lista_letras = list(palabra)
            set_letras = list(set(lista_letras))
            # For que recorra las letras sin repetir
            for letra in set_letras:
                contador = 0
                # For que cuente las veces que aparece cada letra
                for caracter in lista_letras:
                    # Condición para que cuente
                    if letra == caracter:
                        contador += 1
                # Agregar letra y respectivas apariciones en la palabra
                dicc_palabra[letra] = contador
            # Agragar diccionario respectivo a cada palabra con las letras repetidas
            dicc_grande[palabra] = dicc_palabra
        return dicc_grande

    def banda_movil(self, mini, maxi):
        """
        Método de la clase AnalizadorTexto para analizar 
        una subfrase del texto original.

        :param mini: Índice de inicio de la subfrase.
        :type mini: int
        :param maxi: Índice de fin de la subfrase.
        :type maxi: int
        :return: Un diccionario con el conteo de cada letra en la subfrase.
        :rtype: dict or str
        """
        # Obtener la frase delimitada y debe cumplir ciertas condiciones
        if mini >= 0 and maxi <= len(self.get_frase) and mini < maxi:
            subfrase = self.get_frase[mini:maxi]  # Obtener la frase cortada con los parametros
            # Separar subfrase en una lista con sus palabras
            lista_palabras = subfrase.split()
            # Crear un string concatenando las palabras (le estoy quitando espacios)
            frase_pegada = "".join(lista_palabras)
            dicc_subfrase = {}
            # Crear una lista con las letras sin repetir
            lista_letras = list(frase_pegada)
            set_letras = list(set(lista_letras))
            # For que recorra las letras sin repetir
            for letra in set_letras:
                contador = 0
                # For que cuente las veces que aparece cada letra
                for caracter in lista_letras:
                    # Condición para que cuente
                    if letra == caracter:
                        contador += 1
                # Agregar letra y respectivas apariciones en la palabra
                dicc_subfrase[letra] = contador
            return dicc_subfrase
        else:
            return "Los parámetros ingresados son inválidos"

    
