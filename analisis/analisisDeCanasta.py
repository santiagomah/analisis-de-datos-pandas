#importar el paquete o paquetes que voy analisar la informacion

import pandas as pd


def anizarCanastaBasica():
    #2 sin importar la fuente (sql, xls, cvs, JSON ....)
    #debeos crear una tabla tabulada que se llama DATAFRAME
    tabla=pd.read_csv('./data/bdcanasta.csv')

    #print (tabla) 
    #aplico flitros para limpiar o seleccionar datos
    #print(tabla.head(25))
    #print(tabla.tail())
    print(tabla.describe())
