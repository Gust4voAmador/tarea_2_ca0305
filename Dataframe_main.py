# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:02:06 2024

@author: AMADOR
"""

import pandas as pd
df_colesterol = pd.read_csv(
    'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv',
    sep = ";"
)
#print(df_colesterol)

from Df import Df

#Hacer que df_colesterol sea un objeto de la clase Df para usar los métodos
df_coles_clase = Df(df_colesterol)

df_colesterol_estadisticas = df_coles_clase.dicc_estadisticas()

#print(df_coles_clase.dicc_estadisticas())


#print(df_coles_clase.caracte_columna("altura"))

print(df_coles_clase.normalizardf(None))

