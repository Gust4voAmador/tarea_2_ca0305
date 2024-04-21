# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:05:32 2024

@author: AMADOR
"""

import pandas as pd
import numpy as np

#Crear la clase Df donde estarán los métodos 
class Df():
    """
    Clase para análisis básico de DataFrames de Pandas.
    
    Args:
        df (pd.DataFrame): DataFrame de Pandas para análisis.

    Attributes:
        num_filas (int): Cantidad de filas en el DataFrame.
        num_columnas (int): Cantidad de columnas en el DataFrame.
        tipo_columnas (dict): Tipos de datos de cada columna en el DataFrame.
        nulos_por_columna (dict): Cantidad de valores nulos por columna en el DataFrame.
        dataframe (pd.DataFrame): DataFrame de Pandas para análisis.
    """
    #constructor
    def __init__(self, df): 
        """
        Constructor de la clase Df.

        Args:
            df (pd.DataFrame): DataFrame de Pandas para análisis.
        """
    
        #Lo siguiente es la creacion de lo atributos
        
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html
        # Obtener numero de filas y columnas
        filas, columnas = df.shape
        
        self.num_filas = filas #Cantidad de filas
        self.num_columnas = columnas #Cantidad de columnas
        
        #tipos de columnas
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
        #Series que contiene los tipos de datos de cada columna en un DataFrame
        tipo_cols = df.dtypes 
        
        #Usar to_dict() para convertir la serie en un diccionario
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
        self.tipo_columnas = tipo_cols.to_dict()
        
        #utilizar el método sum() después de aplicar la función isnull(), esto
        #para sumar las veces que sea null por columnas, devuelve una serie
        #https://docs.kanaries.net/es/topics/Pandas/pandas-where 
        null_columna = df.isnull().sum()
        self.nulos_por_columna = null_columna.to_dict()
        
        #El DataFrame
        self.dataframe = df
        
    # Métodos getter
    @property
    def get_cantidad_columnas(self):
        """Obtiene la cantidad de columnas en el DataFrame."""
        return self.num_columnas

    @property
    def get_cantidad_filas(self):
        """Obtiene la cantidad de filas en el DataFrame."""
        return self.num_filas

    @property
    def get_tipo_columnas(self):
        """Obtiene los tipos de datos de cada columna en el DataFrame."""
        return self.tipo_columnas
    
    @property
    def get_nulos_por_columna(self):
        """Obtiene la cantidad de valores nulos por columna en el DataFrame."""
        return self.nulos_por_columna
    
    @property
    def get_dataframe(self):
        """Obtiene el DataFrame de Pandas."""
        return self.dataframe

    # Métodos setter
    @get_cantidad_columnas.setter
    def set_cantidad_columnas(self, cantidad_columnas):
        """Establece la cantidad de columnas en el DataFrame."""
        self.num_columnas = cantidad_columnas

    @get_cantidad_filas.setter
    def set_cantidad_filas(self, cantidad_filas):
        """Establece la cantidad de filas en el DataFrame."""
        self.num_filas = cantidad_filas

    @get_tipo_columnas.setter
    def set_tipo_columnas(self, tipo_columnas):
        """Establece los tipos de datos de cada columna en el DataFrame."""
        self.tipo_columnas = tipo_columnas
    
    @get_nulos_por_columna.setter
    def set_nulos_por_columna(self, nulos_por_columna):
        """Establece la cantidad de valores nulos por columna en el DataFrame."""
        self.nulos_por_columna = nulos_por_columna
    
    @get_dataframe.setter
    def set_dataframe(self, dataframe):
        """Establece el DataFrame de Pandas."""
        self.dataframe = dataframe

    #Crear metodo que devuelva el diccionario con las estadísticas 
    def dicc_estadisticas(self):
        """
    Devuelve un diccionario con estadísticas básicas del DataFrame.

    Returns:
        dict: Diccionario con las estadísticas del DataFrame. Las estadísticas incluyen:
            -Cantidad total de filas en el DataFrame.
            -Cantidad total de columnas en el DataFrame.
            -Tipos de datos de cada columna en el DataFrame.
            -Cantidad de valores nulos por columna en el DataFrame.

    Raises:
        None
    """
        
        #crear diccionario con ayuda de los gets
        estadis = {
        'cantidad_filas': self.get_cantidad_filas,
        'cantidad_columnas': self.get_cantidad_columnas,
        'tipos_columnas': self.get_tipo_columnas,
        'valores_nulos_por_columna': self.get_nulos_por_columna
        }
        return estadis

    #Crear metodo para características columna
    #Tiene como parámetro la columna y el objeto Df
    def caracte_columna(self,col):
        """
        Devuelve características básicas de una columna específica del DataFrame.
    
        Args:
            col (str): Nombre de la columna a analizar.
    
        Returns:
            dict: Diccionario con las características de la columna. Las características dependen del tipo de columna:
                - Si la columna es numérica, se incluyen: 
                    - 'Tipo de columna': Tipo de datos de la columna.
                    - 'Promedio': Promedio de los valores en la columna.
                    - 'Mediana': Mediana de los valores en la columna.
                    - 'Valor Máximo': Valor máximo en la columna.
                    - 'Valor Mínimo': Valor mínimo en la columna.
                    - 'Desviación estándar': Desviación estándar de los valores en la columna.
                - Si la columna no es numérica, se incluyen: 
                    - 'Tipo de columna': Tipo de datos de la columna.
                    - 'Moda': Valor más frecuente en la columna.
    
        Raises:
            ValueError: Si el nombre de la columna no es válido o si la columna indicada no existe en el DataFrame.
        """
        
        #Obtener el DataFrame del objeto
        dataf = self.get_dataframe
        
        # Obtener una lista de los nombres de las columnas
        #https://ioflood.com/blog/dataframe-to-list-pandas/
        lista_columnas = dataf.columns.tolist()
        
        
        #Verificar que el nombre ingresado sea una columna
        if not col in lista_columnas:
            raise ValueError("La columna ingresada no existe")

        #verificar que lo ingresado es un string
        if not isinstance(col, str):
            raise ValueError("Debe ingresar el nombre (string) de la columna que desea analizar")
        
        #Obtener el tipo de col de la serie del metodo dtypes de pd ya usado
        tipo_col = dataf.dtypes[col]
        
        #Verificar si es de tipo int o float para sacar media, mediana, etc...
        if np.issubdtype(tipo_col, np.number):
            
            #Obtener el promedio de la columna 
            #https://docs.kanaries.net/es/topics/Pandas/pandas-mean
            media = dataf[col].mean()
            
            #obtener la mediana
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html#pandas.DataFrame.median
            mediana = dataf[col].median()
            
            #Obtener el maximo y minimo de la columna
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min
            maxi = dataf[col].max()
            mini = dataf[col].min()

            #Obtener desviación estandar
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std
            desviacion = dataf[col].std()
            
            dicc_caracts_colo = {
                'Tipo de columna': tipo_col,
                'Promedio': media,
                'Mediana' : mediana,
                'Valor Máximo' : maxi,
                'Valor Mínimo' : mini,
                'Desviación estándar' : desviacion
            }
            
            
            return dicc_caracts_colo

        else:
            #obtener moda como serie
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas-dataframe-mode
            moda_s = dataf[col].mode()
            
            #obtener la primera moda de la serie
            moda = moda_s.iloc[0]
            
            
            dicc_caracts_colo = {
                'Tipo de columna': tipo_col,
                'Moda' : moda
            }
            
            return dicc_caracts_colo
        
    #La funcion tene col como None para indicar que es todo el df, y si tiene 
    #el nombre de una columna entonces lo hace para esa columna
    def normalizardf(self,col = None):
        """
        Normaliza los valores de las columnas numéricas en el DataFrame.
    
        Args:
            col (str, optional): Nombre de la columna a normalizar. Si es None, se normalizan todas las columnas numéricas del DataFrame. Por defecto es None.
    
        Returns:
            str: Una cadena de texto que indica que las columnas numéricas han sido normalizadas y devuelve el DataFrame con esas columnas normalizadas.
    
        Raises:
            ValueError: Si el nombre de la columna no es válido o si la columna indicada no contiene valores numéricos.
        """
        
        #extraer df
        dataf = self.get_dataframe
        
        #Si se indica columna se hace para la idicada
        if not col is None:
            #verificar que col sea string
            if not isinstance(col, str):
                raise ValueError("Debe ingresar el nombre (string) de la columna que desea analizar")
            
            #Verificar que la columna sea numerable para normaliza
            if not np.issubdtype(dataf[col].dtypes, np.number):
                raise ValueError("La columna indicada debe ser con elementos del tipo numerables")
                
            # Normalizar todo el dataf utilizando la formula de maximo y mínimo
            # https://www.diegocalvo.es/normalizar-dataframes-en-python/
            df_normalizado = (dataf[col] - dataf[col].min()) / (dataf[col].max() - dataf[col].min())
        
        #si no se indica columna entonces se hace para todo el df
        else:
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
            # Filtrar solo las columnas numéricas e ignorar las demás
            df_num = dataf.select_dtypes(include='number')
            
            # Normalizar todo el dataframe 
            df_normalizado = (df_num - df_num.min()) / (df_num.max() - df_num.min())

        return f'La columna {col} normalizada es: \n {df_normalizado} '
        
        
        
        
        
        
        
        
        
        
        
        
        
        