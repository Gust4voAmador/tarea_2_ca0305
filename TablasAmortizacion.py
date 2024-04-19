# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:59:17 2024

@author: AMADOR
"""

#https://pypi.org/project/amortization/
import pandas as pd
from amortization.schedule import amortization_schedule

class TablaAmortizacionFija():
    #constructor
    #Donde monto:principal, tasa_anual: tasa de interés anual fija (entre 0 y 1)
    #periodos: numero de años del prestamo
    
    def __init__(self, monto,tasa_anual , periodos ):
        
        #Validar parámetros
        if (monto <= 0) or (tasa_anual > 1 or tasa_anual < 0) or (periodos <= 0):
            raise ValueError("Parámetro inválido")
                
        # Generar la tabla de amortización con ayuda de la librería
        table = amortization_schedule(monto, tasa_anual,  periodos)
        
        # Convertir la tabla en un DataFrame de pandas
        df = pd.DataFrame(table, columns=["Number", "Amount", "Interest", "Principal", "Balance"])
        
        #atributos publicos
        self.dataframe = df
        self.monto = monto
        self.tasa_anual = tasa_anual
        self.periodos = tasa_anual
    
    #Metodos Get publicos
    def get_dataframe(self):
        return self.dataframe
    
    def get_monto(self):
        return self.monto

    def get_tasa_anual(self):
        return self.tasa_anual
    
    def get_periodos(self):
        return self.periodos
    
    #metodo str
    def __str__(self):
        
        #Crear string con una frase y que imprima el df de la tabla
        tabla_str = f'{self.get_dataframe()}'
        return tabla_str
    
    
    
tabla = TablaAmortizacionFija(150000, 0.1, 36)   

print(tabla)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    