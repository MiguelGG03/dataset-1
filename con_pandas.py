from numpy import append
import pandas as pd


"""
-Crear, leer y escribir(No puede trabajar con datos si no puede leerlos)
-Indexación, selección y asignación(Los científicos de datos profesionales
hacen esto docenas de veces al día)
-Resumen de funciones y mapas(Extraiga conocimientos de sus datos)
-Agrupación y clasificación(Aumente su nivel de conocimiento. Cuanto
 más complejo es el conjunto de datos, más importa esto)
-Tipos de datos y valores perdidos(Lidiar con los problemas
 de bloqueo de progreso más comunes)
-Renombrar y combinar(Los datos provienen de muchas fuentes.
 Ayude a que todo tenga sentido juntos)

"""

#Lectura y escritura


df = pd.read_csv('vehicles(20k).csv')
hf= df.head(10)



print("==================================================")
print("           Informacion. Sobre el CSV")
print("==================================================")
print()
print(df.info())
print()



print("==================================================")
print("         Primeras 10 lineas del fichero CSV")
print("==================================================")
print()
print(hf)
print()



print("==================================================")
print("             Indexacion y seleccion")
print("==================================================")
print()
print(df.index)
print()
#dd=int(input("Fila inicial (0/20000): "))
#ad=int(input("Fila final(ad>dd/20000): "))
lista=[]
for i in range(10,21):
    lista.append(i)
print(df.iloc[lista])
print()



print("==================================================")
print("         Resumen de funciones y mapas")
print("==================================================")
print()
print("COUNT\n==================================================")
print(df.count())
print("SUM\n==================================================")
print(df.sum(numeric_only=True))
print("MIN\n==================================================")
print(df.min(numeric_only=True))
print("MAX\n==================================================")
print(df.max(numeric_only=True))
print("MEAN\n==================================================")
print(df.mean(numeric_only=True))
print("STANDARD DEVIATION\n==================================================")
print(df.std(numeric_only=True))
print("DESCRIBE\n==================================================")
print(df.describe())



print("==================================================")
print("          Agrupación y clasificación")
print("==================================================")
print()
print("COCHES DE TEXAS")
print()
df_tx=df.groupby(["state"]).get_group("tx")
print(df_tx)
print(df_tx.describe())



print("==================================================")
print("         Tipos de datos y valores perdidos")
print("==================================================")
print()
s_year=df["year"]
print(s_year.count())
print(df.count())
print("Se puede observar que hay coches que tienen el año a nulo, porque\n"+
       "el numero de ID's no es el mismo que el de años registrados")



print("==================================================")
print("               Renombrar y combinar")
print("==================================================")
print()
ef=df.rename(columns={"county": "condado", "state": "estado","year":"año"})
print(ef.tail(10))
s_c=ef["condado"]
s_e=ef["estado"]
s_a=ef["año"]
print(s_c.head(1))
print(s_e.head(1))
print(s_a.head(1))