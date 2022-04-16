class data:
    def __init__(self):
        ruta = input('Escriba la ruta en la que se encuentra su archivo: ')
        f = open(ruta, 'r')
        lista = []
        self.f = f
        self.lista = lista
    
    def crear_lista(self):
        for i in self.f:
            i = i.rstrip('\n')
            columnas = i.split(';')
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

datos = data()
datos.mejorar()
print(datos.lista)