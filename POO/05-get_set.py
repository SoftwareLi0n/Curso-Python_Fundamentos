class Restaurante:

    def __init__(self, nombre, categoria, localidad):
        self.nombre = nombre
        self.categoria = categoria
        self.__localidad = localidad # public, protecte, privado

    def mostrar_datos(self):
        print(f'Restaurante: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Localidad: {self.__localidad}')

    # get = obtener, set = asignar
    def get_localidad(self):
        return self.__localidad

    def set_localidad(self, localidad):
        self.__localidad = localidad

r1 = Restaurante('Software Lion', 'Comida Rápida', 'Perú')
# Obtener localidad
localidad = r1.get_localidad()
print(localidad)

# Cambiar localidad
r1.set_localidad('Venezuela')
r1.mostrar_datos()