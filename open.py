import numpy as np
import pandas as pd
import argparse

import matplotlib.pyplot as plt

"""
Code for reading the COVID main datafile from DGE
"""


parser = argparse.ArgumentParser()
parser.add_argument("-a")

p = parser.parse_args()

data = pd.DataFrame(pd.read_csv(p.a))
drop_columns = ["FECHA_ACTUALIZACION","ID_REGISTRO","ORIGEN","SECTOR","ENTIDAD_UM","NACIONALIDAD","EMBARAZO","HABLA_LENGUA_INDIG","INDIGENA","DIABETES","ASMA","INMUSUPR","HIPERTENSION","OTRA_COM","CARDIOVASCULAR","OBESIDAD","RENAL_CRONICA","TABAQUISMO","OTRO_CASO","MIGRANTE","PAIS_NACIONALIDAD","PAIS_ORIGEN","ENTIDAD_NAC"]

year = p.a[-8:-4]
cdmx = data[data["ENTIDAD_RES"] == 9]
edo = data[data["ENTIDAD_RES"] == 15]

cdmx = cdmx.drop(labels=drop_columns,axis=1)
edo = edo.drop(labels=drop_columns,axis=1)

lista_mun = [2,9,10,11,13,15,16,17,20,22,23,24,25,28,29,30,31,33,34,35,36,37,38,39,44,46,50,53,57,58,59,60,61,65,68,69,70,75,81,83,84,89,91,92,93,94,95,96,99,100,103,104,108,109,112,120,121,122,125]
edozm = edo[edo["MUNICIPIO_RES"].isin(lista_mun)]

zm = pd.merge(cdmx,edozm,how="outer")

zm.to_csv("zm"+year+".csv",index=False)
#print(cdmx.shape)
#print(edozm.shape)
#print(zm.shape)

#print(zm.head())


#def pos(row):
#    column = "CLASIFICACION_FINAL_COVID"
#    if row[column] in (1,2,3,4,5,6):
#        return 1
#    return 0

#def flu(row):
#    column = "CLASIFICACION_FINAL_FLU"
#    if row[column] in (3,4,5,6):
#        return 1
#    return 0


#print("Size of CDMX + EDO: ")
#print(cdmx_edo.shape)

#cdmx_edo["POS"] = cdmx_edo.apply(pos,axis=1)
#cdmx_edo["POS_FLU"] = cdmx_edo.apply(flu,axis=1)
#cases_input = cdmx_edo[["FECHA_SINTOMAS","POS"]].groupby(["FECHA_SINTOMAS"]).sum()


#cases_input.plot(kind="bar")
#plt.show()




