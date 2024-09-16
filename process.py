import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import tables 

#Importing data frames
data = pd.DataFrame(pd.read_csv("zm2020.csv"))
data21 = pd.DataFrame(pd.read_csv("zm2021.csv"))
data22 = pd.DataFrame(pd.read_csv("zm2022.csv"))
data23 = pd.DataFrame(pd.read_csv("zm2023.csv"))
data24 = pd.DataFrame(pd.read_csv("zm2024.csv"))

df20 = tables.Extract(data)
df21 = tables.Extract(data21)
df22 = tables.Extract(data22)
df23 = tables.Extract(data23)
df24 = tables.Extract(data24)


#a1 = pd.concat([df20.cases(),df21.cases()]).sort_index()
Mcases = tables.Merge(df20.cases(),df21.cases(),df22.cases(),df23.cases(),df24.cases_covid_flu()).upto()
Mdeaths = tables.Merge(df20.deaths(),df21.deaths(),df22.deaths(),df23.deaths(),df24.deaths_covid_flu()).upto()
Mhosp = tables.Merge(df20.hospitalized(),df21.hospitalized(),df22.hospitalized(),df23.hospitalized(),df24.hospitalized_covid_flu()).upto()
Micu = tables.Merge(df20.ICU(),df21.ICU(),df22.ICU(),df23.ICU(),df24.ICU_covid_flu()).upto()
Mtubed = tables.Merge(df20.intub(),df21.intub(),df22.intub(),df23.intub(),df24.intub_covid_flu()).upto()


Maestra = tables.Create_Table(Mcases,Mdeaths,Mhosp,Micu,Mtubed).merged()

Maestra.to_csv("Mexico_cases.csv")
###FOR PLOTTING THE RESULTS IF SOMETHING IS NEEDED

#plt.plot(df20.ICU().index,df20.ICU()["ICU"],lw=0.3,color="black")
#plt.plot(df21.ICU().index,df21.ICU()["ICU"],lw=0.3,color="black")
#plt.plot(c2021.index,c2021["Confirmed_cases"],lw=0.3,color="black")
#plt.plot(d2020.index,d2020["ICU"],lw=0.3,color="black")
#plt.plot(d2021.index,d2021["ICU"],lw=0.3,color="black")
#plt.plot(h2020.index,h2020["Hospitalized"])
#plt.savefig("test.pdf",dpi=1000)
#plt.ylim(0,)
#plt.show()