import pandas as pd


df = pd.read_csv('vehicles(20k).csv')
hf= df.head(10)


clomnas=[]
lista=[]


print("==================================================")
print("           Informacion. Sobre el CSV")
print("==================================================")
print()
print(df.info())


print("==================================================")
print("      Primeras 10 lineas del fichero CSV")
print("==================================================")
print()
print(hf)