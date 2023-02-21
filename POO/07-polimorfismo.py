# POLI-MORFISMO
# EJEMPLO: PERRO-MASCOTA

class Perro:
    def __init__(self, raza, nro_patas, categoria):
        self.raza = raza
        self.nro_patas = nro_patas
        self.categoria = categoria

    def guardar(self):
        print('Perrito registrado')

    def mostrar_informacion(self):
        print(f'Soy un perrito sin dueño: {self.raza} y soy {self.categoria}')


class Mascota(Perro):
    def __init__(self, raza, nro_patas, categoria, nombre, edad):
        super().__init__(raza, nro_patas, categoria)
        self.nombre = nombre
        self.edad = edad

    def cambiar_estado(self):
        print('Cambiando estado en la DB')

    def mostrar_informacion(self):
        print(f'Ya tengo dueño y me llamo: {self.nombre}')

    

perro = Perro('Putbull', 4, 'manzo')
perro.guardar()
perro.mostrar_informacion()

print('*******************')

mascota = Mascota('Pitbull', 4, 'manzo', 'matrix', 1)
mascota.cambiar_estado()
mascota.mostrar_informacion()