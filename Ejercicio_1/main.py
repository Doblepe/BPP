
import pandas as pd
import matplotlib.pyplot as plt
try:
    #Compruebo si se puede abrir el fichero
    fichero = open("finanzas2020[1].csv")
except IOError as err:
    print(err)

data= pd.read_table("finanzas2020[1].csv")

total_cols=len(data.axes[1])
print(total_cols)
try: 
    #Compruebo si se puede abrir el fichero
    assert len(data.axes[1]) != 12, "El gŕafico no tiene las doce columnas"
except AssertionError as msg:
        print(msg)


data['Enero'] = data['Enero'].str.replace("'", " ")
enero = data['Enero'].astype('int')
enero = enero.sum()
febrero = data['Febrero'].sum()
marzo = data['Marzo'].sum()
abril = data['Abril'].sum()
mayo = data['Mayo'].sum()
junio = data['Junio'].sum()
data['Julio'] = data['Julio'].str.replace("'", " ")
julio = data['Julio'].astype('int')
julio = julio.sum()
agosto = data['Agosto'].sum()
data['Septiembre'] = data['Septiembre'].str.replace("bug", "0")
septiembre = data['Septiembre'].astype('int')
septiembre = septiembre.sum()
data['Octubre'] = data['Octubre'].str.replace("ups", "0")
octubre = data['Octubre'].astype('int')
octubre = octubre.sum()
data['Noviembre'] = data['Noviembre'].str.replace("'", " ")
noviembre = data['Noviembre'].astype('int')
noviembre = noviembre.sum()
diciembre = data['Diciembre'].sum()

print(f"Enero = {enero}, Febrero = {febrero}, Marzo = {marzo}, Abril = {abril}, Mayo = {mayo}, junio = {junio}, julio = {julio}, agosto ={agosto}, septiembre = {septiembre} octubre = {octubre}, noviembre = {noviembre}, diciembre = {diciembre}")

#¿Qué mes ha ahorrado más?
anio = {"enero": enero, "febrero": febrero, "marzo": marzo, "abril":abril, "mayo": mayo, "junio": junio, "julio": julio, "agosto": agosto, 'septiembre': septiembre, "octubre": octubre, "noviembre": noviembre, "diciembre":diciembre}
#max_anio = max(año.values())
max_anio = max(anio, key=anio.get)
print(f"{max_anio} ha ahorrado más")
#Qué mes ha gastado más?
min_anio = min(anio, key=anio.get)
print(f"{min_anio} ha gastado más")
#Cuál es la media de gasto?
media_de_gasto = sum(anio.values()) / anio.__len__()
print(f"{media_de_gasto} media_de_gasto")
#Cuál ha sido el gasto total
meses_ahorro = []
meses_gasto = []
for  value in anio.values(): 
    if  value < 0:
         meses_gasto.append(value)
    else:
        meses_ahorro.append(value)
print(f"{sum(meses_ahorro)} han sido los ahorros")
print(f"{sum(meses_gasto)} han sido los gastos")

#grafica
fig, ax = plt.subplots()
ax.plot(range(len(anio)),  list(anio.values()))
plt.show()











