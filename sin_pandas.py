class data:
    def __init__(self):
        f = open('vehicles(1000).csv', 'r')
        lista = []
        self.f = f
        self.lista = lista
    
    def crear_lista(self):
        for i in self.f:
            i = i.rstrip('\n')
            columnas = i.split(',')
            if len(columnas) < 25:
                for i in range(26-len(columnas)):
                    columnas.append('')
            self.lista.append(columnas)
        del self.lista[0]
        return self.lista
    
    def mejorar(self):
        self.crear_lista()
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                if self.lista[i][j] == '':
                    self.lista[i][j] = 0
        return self.lista
    
    def parametros(self, parametro, columna):
        self.mejorar()
        for i in range(len(self.lista)):
            parametro.append(self.lista[i][columna])
        return parametro 

datos = data()
id = datos.parametros([], 0)
print(id, '\n')
url = datos.parametros([], 1)
print(url, '\n')
region = datos.parametros([], 2)
print(region, '\n')
region_url = datos.parametros([], 3)
print(region_url, '\n')
price = datos.parametros([], 4)
print(price, '\n')
year = datos.parametros([], 5)
print(year, '\n')
manufacturer = datos.parametros([], 6)
print(manufacturer, '\n')
model = datos.parametros([], 7)
print(model, '\n')
condition = datos.parametros([], 8)
print(condition, '\n')
cylinders = datos.parametros([], 9)
print(cylinders, '\n')
fuel = datos.parametros([], 10)
print(fuel, '\n')
odometer = datos.parametros([], 11)
print(odometer, '\n')
title_status = datos.parametros([], 12)
print(title_status, '\n')
transmission = datos.parametros([], 13)
print(transmission, '\n')
vin = datos.parametros([], 14)
print(vin, '\n')
drive = datos.parametros([], 15)
print(drive, '\n')
size = datos.parametros([], 16)
print(size, '\n')
type = datos.parametros([], 17)
print(type, '\n')
paint_color = datos.parametros([], 18)
print(paint_color, '\n')
image_url = datos.parametros([], 19)
print(image_url, '\n')
description = datos.parametros([], 20)
print(description, '\n')
county = datos.parametros([], 21)
print(county, '\n')
state = datos.parametros([], 22)
print(state, '\n')
lat = datos.parametros([], 23)
print(lat, '\n')
long = datos.parametros([], 24)
print(long, '\n')
posting_date = datos.parametros([], 25)
print(posting_date)