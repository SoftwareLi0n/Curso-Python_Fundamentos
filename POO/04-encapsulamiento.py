class Restaurante:

    def __init__(self, nombre, categoria, localidad):
        self.nombre = nombre
        self.categoria = categoria
        self.__localidad = localidad # public, protecte, privado

    def mostrar_datos(self):
        print(f'Restaurante: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Localidad: {self.__localidad}')


r1 = Restaurante('Software Lion', 'Comida Rápida', 'Perú')
print(r1.__localidad)
r1.mostrar_datos()