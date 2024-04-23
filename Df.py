# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:05:32 2024

@author: AMADOR
"""

import pandas as pd
import numpy as np
import statistics

#Crear la clase Df donde estarán los métodos 
class Df():
    """
    Clase para análisis básico de DataFrames de Pandas.
    
    Args:
        df (pd.DataFrame): DataFrame de Pandas para análisis.

    Attributes:
        _num_filas (int): Cantidad de filas en el DataFrame.
        _num_columnas (int): Cantidad de columnas en el DataFrame.
        _tipo_columnas (dict): Tipos de datos de cada columna en el DataFrame.
        _nulos_por_columna (dict): Cantidad de valores nulos por columna en el DataFrame.
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
        
        self._num_filas = filas #Cantidad de filas
        self._num_columnas = columnas #Cantidad de columnas
        
        #tipos de columnas
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
        #Series que contiene los tipos de datos de cada columna en un DataFrame
        tipo_cols = df.dtypes 
        
        #Usar to_dict() para convertir la serie en un diccionario
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
        self._tipo_columnas = tipo_cols.to_dict()
        
        #utilizar el método sum() después de aplicar la función isnull(), esto
        #para sumar las veces que sea null por columnas, devuelve una serie
        #https://docs.kanaries.net/es/topics/Pandas/pandas-where 
        null_columna = df.isnull().sum()
        self._nulos_por_columna = null_columna.to_dict()
        
        #El DataFrame
        self._dataframe = df
        
    # Métodos getter
    @property
    def num_columnas(self):
        """Obtiene la cantidad de columnas en el DataFrame."""
        return self._num_columnas

    @property
    def num_filas(self):
        """Obtiene la cantidad de filas en el DataFrame."""
        return self._num_filas

    @property
    def tipo_columnas(self):
        """Obtiene los tipos de datos de cada columna en el DataFrame."""
        return self._tipo_columnas
    
    @property
    def nulos_por_columna(self):
        """Obtiene la cantidad de valores nulos por columna en el DataFrame."""
        return self._nulos_por_columna
    
    @property
    def dataframe(self):
        """Obtiene el DataFrame de Pandas."""
        return self._dataframe

    # Métodos setter
    @num_columnas.setter
    def num_columnas(self, cantidad_columnas):
        """Establece la cantidad de columnas en el DataFrame."""
        self._num_columnas = cantidad_columnas

    @num_filas.setter
    def num_filas(self, cantidad_filas):
        """Establece la cantidad de filas en el DataFrame."""
        self._num_filas = cantidad_filas

    @tipo_columnas.setter
    def tipo_columnas(self, tipo_columnas):
        """Establece los tipos de datos de cada columna en el DataFrame."""
        self._tipo_columnas = tipo_columnas
    
    @nulos_por_columna.setter
    def nulos_por_columna(self, nulos_por_columna):
        """Establece la cantidad de valores nulos por columna en el DataFrame."""
        self._nulos_por_columna = nulos_por_columna
    
    @dataframe.setter
    def dataframe(self, dataframe):
        """Establece el DataFrame de Pandas."""
        self._dataframe = dataframe

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
        'cantidad_filas': self.num_filas,
        'cantidad_columnas': self.num_columnas,
        'tipos_columnas': self.tipo_columnas,
        'valores_nulos_por_columna': self.nulos_por_columna
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
        dataf = self.dataframe
        
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
        dataf = self.dataframe
        
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
        
        
    def zscore(self, columna, umbral=3):   
        """
        Método privado para detecta outliers en una columna de un DataFrame 
        utilizando el método Z-Score.El método Z-Score es una técnica 
        estadística para identificar valores atípicos en un conjunto de datos. 
        Calcula cuántas desviaciones estándar un dato está por encima o por 
        debajo de la media. Si el Z-Score es mayor que un umbral 
        (comúnmente 2, 2.5 o 3), el dato se considera atípico. Este método es 
        útil para detectar valores extremos en los datos.
    
        Args:
            df (DataFrame): DataFrame que contiene los datos.
            columna (str): Nombre de la columna que se quiere analizar.
            umbral (float, opcional): Umbral para considerar un valor como 
            outlier basado en Z-Score.
                Por defecto es 3.
    
        Returns:
            list: Lista de valores atípicos detectados.
    
        Raises:
            ValueError: Si la columna especificada no existe en el DataFrame 
            o si el umbral es menor o igual a 0.
        """
        # Obtener el df
        df = self.dataframe
        
        # Verificar si la columna especificada existe en el df
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    
        # Extraer los datos de la columna excluyendo los  NA
        datos = df[columna].dropna().tolist()
    
        
    
        # Verificar si el umbral es válido
        if umbral <= 0:
            raise ValueError("El umbral debe ser mayor que 0")
    
        # Calcular la media y la desviación estándar de los datos
        media = np.mean(datos)
        desviacion_estandar = np.std(datos)
    
        # Calcular el Z-Score para cada dato
        z_scores = [(dato - media) / desviacion_estandar for dato in datos]
    
        # Identificar los dato atípicos basados en el umbral de Z-Score
        outliers = [dato for dato, z_score in zip(datos, z_scores) if abs(z_score) > umbral]
    
        return outliers
    
        
    def iqr_outliers(self, columna):
        """
        Detecta outliers en una columna de un DataFrame utilizando el método del Rango Intercuartílico (IQR).
    
        Args:
            df (DataFrame): DataFrame que contiene los datos.
            columna (str): Nombre de la columna que se quiere analizar.
    
        Returns:
            list: Lista de valores atípicos detectados.
    
        Raises:
            ValueError: Si la columna especificada no existe en el DataFrame.
        """
        # Obtener el df
        df = self.dataframe
    
        # Verificar si la columna especificada existe en el df
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    
        # Extraer los datos de la columna sin tomar los valores NA
        datos = df[columna].dropna().tolist()
    
        # Calcular el primer y tercer cuartil
        q1, q3 = np.percentile(datos, [25, 75])
    
        # Calcular el rango entre los cuartiles
        iqr = q3 - q1
    
        # Definir los límites para identificar los atípicos
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
    
        # Identificar los valores atípicos con for
        outliers = []
        for dato in datos:
            if dato < limite_inferior or dato > limite_superior:
                outliers.append(dato)
    
        return outliers
        
        
        
    def std_dev_outliers(self, columna, umbral=3):
        """
        Detecta outliers en una columna de un DataFrame utilizando el método de Desviación Estándar.
    
        Args:
            df (DataFrame): DataFrame que contiene los datos.
            columna (str): Nombre de la columna que se quiere analizar.
            umbral (float, opcional): Umbral para considerar un valor como outlier basado en Desviación Estándar.
                Por defecto es 3.
    
        Returns:
            list: Lista de valores atípicos detectados.
    
        Raises:
            ValueError: Si la columna especificada no existe en el DataFrame o si el umbral es menor o igual a 0.
        """
        # Obtener el df
        df = self.dataframe
        
        # Verificar si la columna especificada existe en el df
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    
        # Extraer los datos de la columna excluyendo los valores NA
        datos = df[columna].dropna().tolist()
    
    
        # Verificar si el umbral es válido
        if umbral <= 0:
            raise ValueError("El umbral debe ser mayor que 0")
    
        # Calcular la media y la desviación estándar de los datos
        media = np.mean(datos)
        desviacion_estandar = np.std(datos)
    
        # Identificar los datos atípicos basados en el umbral de dv stan
        outliers = []
        for dato in datos:
            if abs(dato - media) > umbral * desviacion_estandar:
                outliers.append(dato)
    
        return outliers        
        
    def tukey_outliers(self, columna):
        """
        Detecta outliers en una columna de un DataFrame utilizando el método de Tukey (Bigotes).
        Calcula el rango intercuartílico (IQR), que es la diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1).
        Define los límites inferior y superior para identificar valores atípicos:
            Límite Inferior: Q1−1.5×IQRQ1−1.5×IQR
            Límite Superior: Q3+1.5×IQRQ3+1.5×IQR
            Cualquier valor por debajo del límite inferior o por encima del límite superior se considera atípico.
    
        Args:
            df (DataFrame): DataFrame que contiene los datos.
            columna (str): Nombre de la columna que se quiere analizar.
    
        Returns:
            list: Lista de valores atípicos detectados.
    
        Raises:
            ValueError: Si la columna especificada no existe en el DataFrame.
        """
        # Obtener el df
        df = self.dataframe
        
        # Verificar si la columna especificada existe en el df
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    
        # Extraer los datos de la columna excluyendo los valores NA
        datos = df[columna].dropna().tolist()
    
        # Calcular el primer y tercer cuartil
        q1, q3 = np.percentile(datos, [25, 75])
    
        # Calcular el rango intercuartílico (IQR)
        iqr = q3 - q1
    
        # Definir los límites para identificar outliers
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
    
        # Identificar los valores atípicos
        outliers = []
        for dato in datos:
            if dato < limite_inferior or dato > limite_superior:
                outliers.append(dato)
    
        return outliers        
        
    def seleccionar_datos_atipicos(self, columna):
        """
        Selecciona los datos atípicos de una columna utilizando cuatro metodologías diferentes y calcula la moda de cada conjunto de valores atípicos.

        Args:
            columna (str): Nombre de la columna del DataFrame para analizar.

        Returns:
            dict: Un diccionario con la información sobre los datos atípicos seleccionados y sus modas.
                Contiene los siguientes elementos:
                    - "Nombre columna": Nombre de la columna analizada.
                    - "Métodos y datos atípicos": Un diccionario que contiene los nombres de los métodos (Z-Score, Rango Intercuartílico, Desviación Estándar y Tukey)
                      como claves y las listas de valores atípicos detectados por cada método como valores.
                    - "Datos atípicos finales": Una lista que contiene la moda de los valores atípicos detectados por cada método.
        """
        
        # Obtener los valores atípicos con ayuda de las funciones privadas
        #creadas anteriormente
        zscore_outliers = self.zscore(columna)
        iqr_outliers = self.iqr_outliers(columna)
        std_dev_outliers = self.std_dev_outliers(columna)
        tukey_outliers = self.tukey_outliers(columna)


        # Para calcular la moda de cada método usamos la funcion de la librería 
        # https://docs.python.org/3/library/statistics.html
        zscore_mode = statistics.mode(zscore_outliers)
        iqr_mode = statistics.mode(iqr_outliers) 
        std_dev_mode = statistics.mode(std_dev_outliers)
        tukey_mode = statistics.mode(tukey_outliers)
        
        # Crear diccionario para los valores atípicos y sus metodos
        
        atipicos = {'zscore' : zscore_outliers,
                    'iqr' : iqr_outliers,
                    'std_dev' : std_dev_outliers,
                    'tukey' : tukey_mode}
        
        
        # Rotornar matriz con la información indicada
        return {
            "Nombre columna": columna,
            "Métodos y datos atípicos": atipicos,
            "Datos atípicos finales": [zscore_mode, iqr_mode, std_dev_mode, tukey_mode]
        }
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        