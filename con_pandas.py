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
dd=int(input("Fila inicial (0/20000): "))
ad=int(input("Fila final(ad>dd/20000): "))
lista=[]
for i in range(dd,ad+1):
    lista.append(i)
print(df.iloc[lista])
print()

print("==================================================")
print("         Resumen de funciones y mapas")
print("==================================================")
