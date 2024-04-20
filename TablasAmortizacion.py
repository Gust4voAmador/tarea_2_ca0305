# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:59:17 2024

@author: AMADOR
"""

#https://pypi.org/project/amortization/
import pandas as pd
from amortization.schedule import amortization_schedule

class TablaAmortizacion():
    #constructor
    #Donde monto:principal, tasa_anual: tasa de interés mensual fija (entre 0 y 1)
    #periodos: numero de meses del prestamo
    
    def __init__(self, periodos,tasa_interes_anual, monto ,tasa_variable):
        
        #Establecer diferencias por defecto (Punto 3 de las indicaciones)
        diferencia_base_primer_ano = -0.02
        diferencia_base_tercero_ymas = 0.04
        
        #convertir tasa anual a mesual
        tasa_interes = ((1+tasa_interes_anual)**(1/12))-1
        
        #Validar parámetros
        if (monto <= 0) or (tasa_interes > 1 or tasa_interes < 0) or (periodos <= 0):
            raise ValueError("Parámetro inválido")
        
        #Velidar el valor ingresado en tasa_variable
        if not isinstance(tasa_variable, bool):
            raise ValueError("El parámetro tasa variable debe ser de tipo bolean")
      
        #iniciar df fuera de los if para que guarde la info
        df = None
        
        #inicializar a df
        if tasa_variable == False:
        
            # Generar la tabla de amortización con ayuda de la librería
            table = amortization_schedule(monto*(1.05), tasa_interes,  periodos)
            
            # Convertir la tabla en un DataFrame de pandas
            df = pd.DataFrame(table, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
            
            # Cambiar el nombre de la columna "Number" a "Periodo"
            df = df.rename(columns={'Number': "Month"})
        
        else:
            
            #Verificar que lo variable de las tasas sean negativas y positivas respectivamente
            if diferencia_base_primer_ano > 0 or diferencia_base_tercero_ymas < 0:
                raise ValueError("Para el primer año ingrese una diferenica negativa y para el tercer año o mas debe ser positiva")
            
            
            #Generar primer año de la tabla (12 periodos)
            #Ajuste de la tasa dado que es +4% anual se hace convergencia a mensual
            table1 = amortization_schedule(monto*(1.05), tasa_interes-(((1+abs(diferencia_base_primer_ano))**(1/12))-1),  periodos)
            # Convertir la tabla en un DataFrame de pandas
            df1 = pd.DataFrame(table1, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
            
            if periodos > 12:
                #Cortar tabla en el periodo 12 (incluyendo)
                #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
                df1= df1.iloc[:12] # 12 para incluir el periodo 12
            
            #agregar el primer año al df inicializado
            df = df1
            
            
            if periodos>= 12:
                #obtener el balance de la fila 12 para iniciar la tabla con otra tasa
                balance1 = df1.iloc[11]["Balance"]
                
                #Generar primer año de la tabla de 12 periodos (segundo año)
                table2 = amortization_schedule(balance1, tasa_interes, periodos-12)
                # Convertir la tabla en un DataFrame de pandas
                df2 = pd.DataFrame(table2, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
            
                #Cortar tabla en el periodo 12 (incluyendo)
                df2= df2.iloc[:12]
                
                # Concatenar los tres DataFrames uno debajo del otro
                df = pd.concat([df1, df2], axis=0)
            
            if periodos >= 24:
                #obtener el balance de la fila 12 (periodo 24) 
                balance2 = df2.iloc[11]["Balance"]
                #Generar primer año de la tabla de 12 periodos (segundo año)
                #Ajuste de la tasa dado que es +4% anual se hace convergencia a mensual
                table3 = amortization_schedule(balance2, tasa_interes+(((1+diferencia_base_tercero_ymas)**(1/12))-1),  periodos-24)
                # Convertir la tabla en un DataFrame de pandas
                df3 = pd.DataFrame(table3, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
                
                # Concatenar los tres DataFrames uno debajo del otro
                df = pd.concat([df1, df2, df3], axis=0)
            
            # Restablecer los índices de df 
            df = df.reset_index(drop=True)
            
            # Cambiar el nombre de la columna "Number" a "Mes"
            df.rename(columns={"Number": "Month"}, inplace=True)
            
            # Llenar la columna "Mes" con números del 1 a n para recetear lo valores
            df["Month"] = range(1, len(df) + 1)
        
        
        
        #atributos publicos
        self.dataframe = df
        self.monto = monto*(1.05)
        self.tasa_base = tasa_interes_anual
        self.periodos = periodos
    
    #Metodos Get publicos
    def get_dataframe(self):
        return self.dataframe
    
    def get_monto(self):
        return self.monto

    def get_tasa_base(self):
        return self.tasa_base
    
    def get_periodos(self):
        return self.periodos
    
    #metodo str
    def __str__(self):
        
        #Crear string con una frase y que imprima el df de la tabla
        tabla_str = f'{self.get_dataframe()}'
        return tabla_str
    
    def estado_credito(self, mes):
        #verificar que el numero del mes sea cuerente
        if not isinstance(mes, int):
            raise ValueError("El número de mes debe de ser tipo int")
            
        if mes < 1 or mes > self.get_periodos():
            raise ValueError(f'Número de mes invalido. Rango de meses es de [1 a {self.get_periodos()}]')
        
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
        # Imprimir la primera fila segun el numero del mes -1 y hacerlo diccio
        dicc = self.get_dataframe().iloc[mes-1].to_dict()
        
        return print(dicc)
    
    #Esta clase hereda de TablaAmortizacion, no obstante se copió bastante del constructor de la de arriab
    #Ya que no encontré otra forma de hacer para disminuir la cantidad de codigo, pero no se pudo
class TablaAmortizacionPersonalizada(TablaAmortizacion):
    
    def __init__(self, periodos,tasa_interes_anual, monto ,tasa_variable, diferencia_year_1,diferencia_year_3):
        
        #convertir tasa anual a mesual
        tasa_interes = ((1+tasa_interes_anual)**(1/12))-1
        
        #Validar parámetros
        if (monto <= 0) or (tasa_interes > 1 or tasa_interes < 0) or (periodos <= 0):
            raise ValueError("Parámetro inválido")
        
        #Velidar el valor ingresado en tasa_variable
        if not isinstance(tasa_variable, bool):
            raise ValueError("El parámetro tasa variable debe ser de tipo bolean")
      
        #iniciar df fuera de los if para que guarde la info
        df = None
        
        #Verificar que lo variable de las tasas sean negativas y positivas respectivamente
        if diferencia_year_1 > 0 or diferencia_year_3 < 0:
            raise ValueError("Para el primer año ingrese una diferenica negativa y para el tercer año o mas debe ser positiva")
        
        
        #Generar primer año de la tabla (12 periodos)
        #Ajuste de la tasa dado que es +4% anual se hace convergencia a mensual
        table1 = amortization_schedule(monto*(1.05), tasa_interes-(((1+abs(diferencia_year_1))**(1/12))-1),  periodos)
        # Convertir la tabla en un DataFrame de pandas
        df1 = pd.DataFrame(table1, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
        
        if periodos > 12:
            #Cortar tabla en el periodo 12 (incluyendo)
            #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
            df1= df1.iloc[:12] # 12 para incluir el periodo 12
        
        #agregar el primer año al df inicializado
        df = df1
        
        
        if periodos>= 12:
            #obtener el balance de la fila 12 para iniciar la tabla con otra tasa
            balance1 = df1.iloc[11]["Balance"]
            
            #Generar primer año de la tabla de 12 periodos (segundo año)
            table2 = amortization_schedule(balance1, tasa_interes, periodos-12)
            # Convertir la tabla en un DataFrame de pandas
            df2 = pd.DataFrame(table2, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
        
            #Cortar tabla en el periodo 12 (incluyendo)
            df2= df2.iloc[:12]
            
            # Concatenar los tres DataFrames uno debajo del otro
            df = pd.concat([df1, df2], axis=0)
        
        if periodos >= 24:
            #obtener el balance de la fila 12 (periodo 24) 
            balance2 = df2.iloc[11]["Balance"]
            #Generar primer año de la tabla de 12 periodos (segundo año)
            #Ajuste de la tasa dado que es +4% anual se hace convergencia a mensual
            table3 = amortization_schedule(balance2, tasa_interes+(((1+diferencia_year_3)**(1/12))-1),  periodos-24)
            # Convertir la tabla en un DataFrame de pandas
            df3 = pd.DataFrame(table3, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
            
            # Concatenar los tres DataFrames uno debajo del otro
            df = pd.concat([df1, df2, df3], axis=0)
        
        # Restablecer los índices de df 
        df = df.reset_index(drop=True)
        
        # Cambiar el nombre de la columna "Number" a "Mes"
        df.rename(columns={"Number": "Month"}, inplace=True)
        
        # Llenar la columna "Mes" con números del 1 a n para recetear lo valores
        df["Month"] = range(1, len(df) + 1)
        
        #atributos publicos nuevos
        self.diferencia_year_1 = diferencia_year_1
        self.diferencia_year_3 = diferencia_year_3
        #Vuelvo a establecer el atributo dataframe
        self.dataframe = df
    
    #Get
    def get_diferencia_tasa_base_year_1(self): 
        return self.diferencia_year_1
        
    def get_diferencia_tasa_base_year_3_mas(self): 
        return self.diferencia_year_3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    