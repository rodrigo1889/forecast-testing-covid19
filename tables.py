import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from functools import reduce


class Extract:
    def __init__(self,table: pd.DataFrame):
        self.data = table
    
    def cases(self):
        conf = self.data[self.data["CLASIFICACION_FINAL"].isin([1,2,3])]
        pos = conf[["FECHA_SINTOMAS","CLASIFICACION_FINAL"]]
        p = pos.groupby("FECHA_SINTOMAS").sum()
        p.columns = ["Confirmed_cases"]
        p.index = pd.to_datetime(p.index)
        return p
    
    def cases_covid_flu(self): #FOR ADDING THE FLU CLASSIFCATION WHEN USING THE 2024 DATA
        conf = self.data[self.data["CLASIFICACION_FINAL_COVID"].isin([1,2,3])]
        conf2 = self.data[self.data["CLASIFICACION_FINAL_FLU"].isin([1,2,3])]
        pos = conf[["FECHA_SINTOMAS","CLASIFICACION_FINAL_COVID"]]
        pos2 = conf2[["FECHA_SINTOMAS","CLASIFICACION_FINAL_FLU"]]
        pos = pos.groupby("FECHA_SINTOMAS").sum()
        pos2 = pos2.groupby("FECHA_SINTOMAS").sum()
        final = pd.merge(pos,pos2,how="outer",left_index=True,right_index=True)
        final["sum"] = final.sum(axis=1)
        final = final[["sum"]]
        final.columns = ["Confimed_cases"]
        final.index = pd.to_datetime(final.index)
        return final
    
    def deaths(self):
        conf = self.data[self.data["CLASIFICACION_FINAL"].isin([1,2,3])]
        deaths = conf[["FECHA_DEF","CLASIFICACION_FINAL"]]
        d = deaths.groupby("FECHA_DEF").sum()
        d.columns = ["Deaths"]
        d = d.drop("9999-99-99",axis=0)
        d.index = pd.to_datetime(d.index)
        return d
    
    def deaths_covid_flu(self): #FOR ADDING THE FLU CLASSIFCATION WHEN USING THE 2024 DATA
        conf = self.data[self.data["CLASIFICACION_FINAL_COVID"].isin([1,2,3])]
        conf2 = self.data[self.data["CLASIFICACION_FINAL_FLU"].isin([1,2,3])]
        pos = conf[["FECHA_DEF","CLASIFICACION_FINAL_COVID"]]
        pos2 = conf2[["FECHA_DEF","CLASIFICACION_FINAL_FLU"]]
        pos = pos.groupby("FECHA_DEF").sum()
        pos2 = pos2.groupby("FECHA_DEF").sum()
        final = pd.merge(pos,pos2,how="outer",left_index=True,right_index=True)
        final["sum"] = final.sum(axis=1)
        final = final[["sum"]]
        final = final.drop("9999-99-99",axis=0)
        final.columns = ["Deaths"]
        final.index = pd.to_datetime(final.index)
        return final

    def hospitalized(self):
        conf = self.data[self.data["CLASIFICACION_FINAL"].isin([1,2,3])]
        hosp = conf[["FECHA_INGRESO","TIPO_PACIENTE"]]
        hosp = hosp[hosp["TIPO_PACIENTE"]==2]
        h = hosp.groupby("FECHA_INGRESO").sum()
        h.columns = ["Hospitalized"]
        h.index = pd.to_datetime(h.index)
        return h
    
    def hospitalized_covid_flu(self): #FOR ADDING THE FLU CLASSIFCATION WHEN USING THE 2024 DATA
        conf = self.data[self.data["CLASIFICACION_FINAL_COVID"].isin([1,2,3])]
        conf2 = self.data[self.data["CLASIFICACION_FINAL_FLU"].isin([1,2,3])]
        pos = conf[["FECHA_INGRESO","TIPO_PACIENTE"]]
        pos2 = conf2[["FECHA_INGRESO","TIPO_PACIENTE"]]
        hosp = pos[pos["TIPO_PACIENTE"]==2]
        hosp2 = pos2[pos2["TIPO_PACIENTE"]==2]
        h = hosp.groupby("FECHA_INGRESO").sum()
        h2 = hosp2.groupby("FECHA_INGRESO").sum()
        final = pd.merge(h,h2,how="outer",left_index=True,right_index=True)
        final["sum"] = final.sum(axis=1)
        final = final[["sum"]]
        #final = final.drop("9999-99-99",axis=0)
        final.columns = ["Hospitalized"]
        final.index = pd.to_datetime(final.index)
        return final
    
    def ICU(self):
        conf = self.data[self.data["CLASIFICACION_FINAL"].isin([1,2,3])]
        icu = conf[conf["UCI"]==1]
        i = icu[["FECHA_INGRESO","UCI"]]
        i = i.groupby("FECHA_INGRESO").sum()
        i.columns = ["ICU"]
        i.index = pd.to_datetime(i.index)
        return i
    
    def ICU_covid_flu(self): #FOR ADDING THE FLU CLASSIFCATION WHEN USING THE 2024 DATA
        conf = self.data[self.data["CLASIFICACION_FINAL_COVID"].isin([1,2,3])]
        conf2 = self.data[self.data["CLASIFICACION_FINAL_FLU"].isin([1,2,3])]
        pos = conf[["FECHA_INGRESO","UCI"]]
        pos2 = conf2[["FECHA_INGRESO","UCI"]]
        hosp = pos[pos["UCI"]==1]
        hosp2 = pos2[pos2["UCI"]==1]
        h = hosp.groupby("FECHA_INGRESO").sum()
        h2 = hosp2.groupby("FECHA_INGRESO").sum()
        final = pd.merge(h,h2,how="outer",left_index=True,right_index=True)
        final["sum"] = final.sum(axis=1)
        final = final[["sum"]]
        #final = final.drop("9999-99-99",axis=0)
        final.columns = ["ICU"]
        final.index = pd.to_datetime(final.index)
        return final
    
    def intub(self):
        conf = self.data[self.data["CLASIFICACION_FINAL"].isin([1,2,3])]
        intub = conf[conf["INTUBADO"]==1]
        i = intub[["FECHA_INGRESO","INTUBADO"]]
        i = i.groupby("FECHA_INGRESO").sum()
        i.columns = ["Intub"]
        i.index = pd.to_datetime(i.index)
        return i
    
    def intub_covid_flu(self): #FOR ADDING THE FLU CLASSIFCATION WHEN USING THE 2024 DATA
        conf = self.data[self.data["CLASIFICACION_FINAL_COVID"].isin([1,2,3])]
        conf2 = self.data[self.data["CLASIFICACION_FINAL_FLU"].isin([1,2,3])]
        pos = conf[["FECHA_INGRESO","INTUBADO"]]
        pos2 = conf2[["FECHA_INGRESO","INTUBADO"]]
        hosp = pos[pos["INTUBADO"]==1]
        hosp2 = pos2[pos2["INTUBADO"]==1]
        h = hosp.groupby("FECHA_INGRESO").sum()
        h2 = hosp2.groupby("FECHA_INGRESO").sum()
        final = pd.merge(h,h2,how="outer",left_index=True,right_index=True)
        final["sum"] = final.sum(axis=1)
        final = final[["sum"]]
        #final = final.drop("9999-99-99",axis=0)
        final.columns = ["Intub"]
        final.index = pd.to_datetime(final.index)
        return final

class Merge:
    def __init__(self,df20,df21,df22,df23,df24):
        self.df20 = df20
        self.df21 = df21
        self.df22 = df22
        self.df23 = df23
        self.df24 = df24
        self.label = self.df20.columns
    
    def obtain_20_21(self):
        m1 = pd.merge(self.df20,self.df21,how="outer",left_index=True,right_index=True,suffixes=("1","2"))
        m1["sum"] = m1.sum(axis=1)
        m1 = m1[["sum"]]
        m1.columns = self.label
        return m1
    
    def obtain_21_22(self):
        m1 = self.obtain_20_21()
        m = pd.merge(m1,self.df22,how="outer",left_index=True,right_index=True,suffixes=("1","2"))
        m["sum"] = m.sum(axis=1)
        m = m[["sum"]]
        m.columns = self.label
        return m
    
    def obtain_22_23(self):
        m1 = self.obtain_21_22()
        m = pd.merge(m1,self.df23,how="outer",left_index=True,right_index=True,suffixes=("1","2"))
        m["sum"] = m.sum(axis=1)
        m = m[["sum"]]
        m.columns = self.label
        return m

    def obtain_23_24(self):
        m1 = self.obtain_22_23()
        m = pd.merge(m1,self.df24,how="outer",left_index=True,right_index=True,suffixes=("1","2"))
        m["sum"] = m.sum(axis=1)
        m = m[["sum"]]
        m.columns = self.label
        return m
    
    def upto(self):
        return self.obtain_23_24()

class Create_Table:
    def __init__(self,cases,deaths,hosp,icu,intub):
        self.cases = cases
        self.deaths = deaths
        self.hosp = hosp
        self.icu = icu
        self.intub = intub
        self.list_ = [self.cases, self.deaths, self.hosp, self.icu, self.intub]
    
    def merged(self):
        df_merged = reduce(lambda left, right: pd.merge(left,right,how="outer",left_index=True,right_index=True),self.list_)
        df_merged = df_merged.fillna(0)
        return df_merged