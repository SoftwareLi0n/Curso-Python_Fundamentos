# Clase Restaurante
# Metodos: Asignar datos, mostrar datos
# Mejorar el código con el constructor

class Restaurante:

    def __init__(self, nombre, categoria, localidad):
        self.nombre = nombre
        self.categoria = categoria
        self.localidad = localidad

    def mostrar_datos(self):
        print(f'Restaurante: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Localidad: {self.localidad}')


r1 = Restaurante('Software Lion', 'Comida Rápida', 'Perú')
r1.mostrar_datos()